# [AutoNotes](https://coltonchrane.dev/)
### Generative Knowledge Engine: Supercharge AI responses by grounding Gemini in your local data for high-precision, context-aware queries.

## 🚀 Features

- **AI-Powered Note Generation**: Automatically converts GitHub issues into formatted markdown notes using Gemini AI.
- **Automated Refinement**: Bot-driven updates to notes via PR comments.
- **Easy Categorization**: Automatically organizes notes into logical directories.

## 🤖 Automation & Tools

This repository uses a **Gemini AI-powered bot** to streamline contributions.

- **`gemini_note_generator.py`**: A Python script that uses Gemini AI (`gemini-3-flash-preview`) to transform raw issue text into clean, structured markdown.
- **`gemini_pr_fixer.py`**: Handles iterative refinements based on PR comments.
- **`issue_to_note.sh`**: A shell utility for basic issue-to-note conversion.

## 🤝 Contributing

We welcome new notes! This repository uses a **Gemini AI-powered bot** to help turn GitHub Issues into formatted technical notes. You don't even need to touch the code—just open an issue.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full details on how to contribute and how the automation works.
