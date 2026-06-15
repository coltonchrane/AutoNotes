# Contributing to AutoNotes

We welcome new notes! This repository uses a **Gemini AI-powered bot** to help turn GitHub Issues into formatted technical notes. You don't even need to touch the code—just open an issue.

## 🚀 Quick Start for Contributors

There are two ways to contribute technical notes:

### Method 1: Use the Contribution Form (Recommended)
The easiest way is to use our **[Contribution Form](https://coltonchrane.dev/AutoNotes/contribute.md)** directly on the website.
1. Fill out the **Category**, **Title**, and **Content**.
2. Click **Generate Note with AI 🤖**.
3. You will be redirected to a pre-filled GitHub Issue. **Click "Submit new issue"** to trigger the automation.

### Method 2: Manually Open a GitHub Issue
1. **Create a New Issue**: Use the [New Issue](https://github.com/coltonchrane/AutoNotes/issues/new) button.
2.  **Format the Title**: Use the format `[Category] Title of your note`. 
    *   *Example: `[Docker] How to clean up unused volumes`*
    *   If you omit the category, Gemini will try to suggest a logical one.
3.  **Write the Body**: Provide the technical details, code blocks, or links in the issue description.
4.  **Add the Label**: Apply the `contribution` label to the issue.

## 🤖 How the Bot Works

Once the `contribution` label is added:
1.  **AI Analysis**: A GitHub Action sends the issue content to Gemini AI (`gemini-3-flash-preview`).
2.  **Formatting**: Gemini cleans up the text, fixes typos, organizes headers with numbered sections, and adds contributor metadata at the bottom.
3.  **Pull Request**: The bot creates a new branch (e.g., `contribution/issue-123`) and opens a Pull Request with the new `.md` file.
4.  **Notification**: The bot comments on your issue with a link to the Pull Request for your review.

### 🔄 Refinement Loop

If the generated note isn't quite right, you can refine it directly in the Pull Request:
1.  **Leave a Comment**: Simply reply to the Pull Request with your feedback (e.g., "Please add a section on X" or "Fix the code example in the second paragraph").
2.  **Bot Update**: The bot will automatically pick up your comment, send it to Gemini along with the current content, and commit the updated version back to the Pull Request branch.
3.  **Reaction**: The bot will add a 🚀 reaction to your comment when the update is complete.

## 🛠️ Repository Setup (For Maintainers)

To ensure the bot functions correctly, the following must be configured in the GitHub repository:

### 1. Gemini API Key
Add your Google AI Studio API key as a repository secret:
*   Go to **Settings** > **Secrets and variables** > **Actions**.
*   Click **New repository secret**.
*   Name: `GEMINI_API_KEY`.
*   Value: *Your API Key*.

### 2. Workflow Permissions
Ensure GitHub Actions has permission to create Pull Requests:
*   Go to **Settings** > **Actions** > **General**.
*   Under **Workflow permissions**, select **Read and write permissions**.
*   Check **Allow GitHub Actions to create and approve pull requests**.

### 3. Labels
Create a label named `contribution` (Case-sensitive) in the **Issues** > **Labels** section.

## 📂 File Structure
Generated notes are placed in directories based on the category (e.g., `Networking/`, `Linux/`). If a category doesn't exist, the bot will create it automatically.

