---
layout: default
title: Gemini CLI Setup and Configuration on Ubuntu
parent: AI & Machine Learning
nav_order: 1
---

# Gemini CLI Setup and Configuration on Ubuntu

This guide provides comprehensive instructions for installing, configuring, and optimizing the Gemini CLI on an Ubuntu system. It covers the setup of the `GEMINI.md` configuration file and provides details on toggling various operational settings for different AI workflows.

## 1. Prerequisites

Before proceeding with the installation, ensure your system is updated and that you have the necessary environment tools installed.

### 1.1 System Update
Update your package list and upgrade existing packages to ensure compatibility:
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Install Python and Pip
Most Gemini CLI implementations rely on Python 3. Ensure you have the Python environment and the package manager (Pip) installed:
```bash
sudo apt install python3 python3-pip python3-venv -y
```

## 2. Installation

To interact with Gemini via the command line, you will typically use the Google Generative AI SDK. It is recommended to use a virtual environment to manage dependencies.

### 2.1 Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv gemini-env
source gemini-env/bin/activate
```

### 2.2 Install the SDK
Install the core library using the following command:
```bash
pip install -q -U google-generativeai
```

## 3. Configuration with GEMINI.md

The `GEMINI.md` file serves as a local configuration manifest to store project-specific instructions, system prompts, and model parameters. This ensures consistency across different sessions.

### 3.1 Creating the Configuration File
Create a file named `GEMINI.md` in your project root to document your preferred settings:

```markdown
# Gemini Project Settings
- **Model**: gemini-1.5-pro
- **Temperature**: 0.7
- **Top_P**: 0.95
- **Max_Tokens**: 2048
- **System_Instruction**: "You are a senior Linux administrator assisting with automation scripts."
```

### 3.2 Authentication
You must export your API Key from [Google AI Studio](https://aistudio.google.com/) to your shell environment. For persistence, add it to your profile:

```bash
# Add to .bashrc for persistence
echo "export API_KEY='your_api_key_here'" >> ~/.bashrc
source ~/.bashrc
```

## 4. Key Parameters and Settings

When configuring the CLI or writing integration scripts, the following parameters are essential for controlling the model's behavior:

| Parameter | Description | Recommended Range |
| :--- | :--- | :--- |
| **Model** | The specific engine version (e.g., `gemini-1.5-pro`, `gemini-1.5-flash`). | N/A |
| **Temperature** | Controls randomness. Higher = creative; lower = deterministic. | 0.0 - 2.0 |
| **Top_P** | Nucleus sampling: selects tokens from the top cumulative probability. | 0.0 - 1.0 |
| **Top_K** | Limits the model's vocabulary to the K most likely tokens. | 1 - 40 |
| **Max Tokens** | The maximum number of tokens to generate in the response. | 1 - 8192+ |

## 5. Toggling Settings

You can toggle settings dynamically depending on your workflow requirements, either via command-line flags or environment aliases.

### 5.1 Command Line Flags
If using a wrapper script or custom CLI tool, implement flags to override default `GEMINI.md` settings:
```bash
# High creativity for brainstorming
gemini-run --temp 0.9 --model gemini-1.5-pro

# Low temperature for technical documentation or code generation
gemini-run --temp 0.1 --model gemini-1.5-flash
```

### 5.2 Environment Toggles
Use aliases in your `~/.bash_aliases` file to switch between predefined operational modes:
```bash
alias gemini-creative='export GEMINI_TEMP=0.9 && export GEMINI_MODEL="gemini-1.5-pro"'
alias gemini-precise='export GEMINI_TEMP=0.1 && export GEMINI_MODEL="gemini-1.5-flash"'
```

## 6. General Information

*   **Rate Limits**: Be aware of the rate limits associated with your API tier. The Free tier has lower RPM (Requests Per Minute) and RPD (Requests Per Day) limits compared to the Pay-as-you-go tier.
*   **Safety Settings**: Gemini includes built-in safety filters for categories like Harassment, Hate Speech, and Sexually Explicit content. These can be adjusted via code to `BLOCK_NONE`, `BLOCK_ONLY_HIGH`, or `BLOCK_MEDIUM_AND_ABOVE`.
*   **Updates**: The Gemini API and SDK evolve rapidly. Regularly update your local libraries:
    ```bash
    pip install --upgrade google-generativeai
    ```

---
**Source:** [GitHub Issue #62](https://github.com/coltonchrane/AutoNotes/issues/62) | **Contributor:** @coltonchrane
---