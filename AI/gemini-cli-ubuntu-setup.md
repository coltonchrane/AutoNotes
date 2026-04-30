---
layout: default
title: Gemini CLI Setup and Configuration on Ubuntu
parent: AI
nav_order: 1
---

# Gemini CLI Setup and Configuration on Ubuntu

This guide provides comprehensive instructions for installing, configuring, and optimizing the Gemini CLI on an Ubuntu system. It covers the setup of the GEMINI.md configuration file and provides details on toggling various operational settings.

## 1. Prerequisites

Before proceeding with the installation, ensure your system is updated and that you have the necessary environment tools.

### 1.1 System Update
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Install Python and Pip
Most Gemini CLI implementations rely on Python. Ensure you have Python 3 and Pip installed:
```bash
sudo apt install python3 python3-pip -y
```

## 2. Installation

To interact with Gemini via the command line, you will typically use the Google Generative AI SDK or a community-driven CLI tool. Install the core library using the following command:

```bash
pip install -q -U google-generativeai
```

## 3. Configuration with GEMINI.md

The `GEMINI.md` file is used to store project-specific instructions and model parameters. This ensures consistency across different sessions.

### 3.1 Creating the Configuration File
Create a file named `GEMINI.md` in your project root to document your settings:

```markdown
# Gemini Project Settings
- Model: gemini-1.5-pro
- Temperature: 0.7
- Top_P: 0.95
- Max_Tokens: 2048
```

### 3.2 Authentication
You must export your API Key from Google AI Studio to your shell environment:

```bash
export API_KEY='your_api_key_here'
# To persist this, add it to your .bashrc
echo "export API_KEY='your_api_key_here'" >> ~/.bashrc
source ~/.bashrc
```

## 4. Key Parameters and Settings

When configuring the CLI or writing scripts, these parameters are essential for controlling the AI's behavior:

### 4.1 Model Selection
*   `gemini-1.5-pro`: High intelligence for complex tasks.
*   `gemini-1.5-flash`: Fast and cost-efficient for high-volume tasks.

### 4.2 Response Controls
*   **Temperature**: Range (0.0 - 2.0). Higher values increase creativity; lower values make responses more deterministic.
*   **Top_K**: Limits the model's vocabulary to the top K most likely tokens.
*   **Top_P**: Also known as nucleus sampling; it selects tokens whose cumulative probability exceeds the threshold P.

## 5. Toggling Settings

You can toggle settings dynamically depending on your workflow requirements.

### 5.1 Command Line Flags
If using a wrapper script, implement toggles to override default `GEMINI.md` settings:
```bash
# Example usage for a creative task
gemini-run --temp 0.9 --model gemini-1.5-pro

# Example usage for a technical/coding task
gemini-run --temp 0.2 --model gemini-1.5-flash
```

### 5.2 Environment Toggles
You can create aliases in your `~/.bash_aliases` file to toggle between modes quickly:
```bash
alias gemini-chat='export GEMINI_MODE="chat"'
alias gemini-code='export GEMINI_MODE="code"'
```

## 6. General Information

*   **Rate Limits**: Be aware of the rate limits associated with your API tier (Free vs. Pay-as-you-go).
*   **Safety Settings**: Gemini has built-in safety filters. You can adjust these in your code to be more or less restrictive depending on your use case.
*   **Updates**: The Gemini API evolves rapidly. Regularly update your local libraries using `pip install --upgrade google-generativeai`.

---
**Source:** [GitHub Issue #62](https://github.com/coltonchrane/AutoNotes/issues/62) | **Contributor:** @coltonchrane