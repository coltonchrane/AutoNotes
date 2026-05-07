#!/usr/bin/env python3
import os
import sys
import json
import re
from google import genai

def apply_changes(changes):
    """
    Applies changes to files.
    'changes' should be a list of dicts: {"path": "...", "content": "..."}
    """
    for change in changes:
        path = change.get("path")
        content = change.get("content")
        if not path or content is None:
            continue
        
        # Ensure directory exists (if not in root)
        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    comment_body = os.environ.get("COMMENT_BODY")
    target_file = os.environ.get("TARGET_FILE") # Might be null if it's a general PR comment

    if not comment_body:
        print("Error: COMMENT_BODY environment variable not set.")
        sys.exit(1)

    # Read PR context
    pr_diff = ""
    if os.path.exists("pr_diff.txt"):
        with open("pr_diff.txt", "r", encoding="utf-8") as f:
            pr_diff = f.read()

    changed_files = []
    if os.path.exists("changed_files.txt"):
        with open("changed_files.txt", "r", encoding="utf-8") as f:
            changed_files = [line.strip() for line in f.readlines() if line.strip()]

    # If target_file is provided (from a review comment), prioritize it
    context_files_info = ""
    for file_path in changed_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    context_files_info += f"\n--- File: {file_path} ---\n{content}\n"
            except Exception as e:
                print(f"Warning: Could not read file {file_path}: {e}")

    model_name = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert software engineer assistant. Your task is to address feedback on a Pull Request.

### Context:
**User Feedback/Comment:**
"{comment_body}"

{"**Specific File Targeted by Comment:** " + target_file if target_file else ""}

**PR Diff:**
```diff
{pr_diff}
```

**Relevant File Contents:**
{context_files_info}

### Instructions:
1. Analyze the feedback and the current state of the code.
2. Determine which files need to be modified to address the feedback.
3. Provide the full updated content for each file that needs changes.
4. If the feedback is documentation-related, maintain the Jekyll front matter and formatting standards of the repo.
5. If the feedback is code-related, ensure the fix is idiomatic and correct.
6. Return your response ONLY as a JSON object with a list of changes.

### Output Format:
{{
  "changes": [
    {{
      "path": "path/to/file.ext",
      "content": "Full updated content of the file..."
    }},
    ...
  ]
}}
"""

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
            }
        )
        
        if not response.text:
            print("Error: Gemini returned an empty response.")
            sys.exit(1)

        text = response.text.strip()
        data = json.loads(text)
        changes = data.get("changes", [])
        
        if not changes:
            print("No changes proposed by Gemini.")
            return

        apply_changes(changes)
        
    except json.JSONDecodeError as je:
        print(f"Error: Failed to parse JSON response from Gemini: {je}")
        print(f"Raw response text: {text if 'text' in locals() else 'N/A'}")
        sys.exit(1)
    except Exception as e:
        print(f"Error calling Gemini API or applying changes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
