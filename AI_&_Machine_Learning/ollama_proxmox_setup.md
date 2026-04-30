---
layout: default
title: Setting up Ollama on Proxmox for Local AI Agents
parent: AI & Machine Learning
nav_order: 1
---

# Setting up Ollama on Proxmox for Local AI Agents

This guide provides a comprehensive walkthrough for installing Ollama on a Proxmox virtual machine and configuring it for use by local network devices and remote agents via Tailscale.

## 1. Proxmox Virtual Machine Setup

To run Ollama efficiently, it is recommended to use a Linux-based Virtual Machine (VM) with dedicated resources. While Ollama can run on CPUs, a GPU is highly recommended for acceptable performance.

### 1.1 VM Configuration Requirements
- **Operating System:** Ubuntu 22.04 or 24.04 LTS (recommended for driver compatibility).
- **CPU:** Use the 'host' CPU type in Proxmox settings to enable AVX/AVX2 instructions.
- **Memory:** Minimum 8GB for small models (7B); 16GB or more for larger models.
- **GPU Passthrough:** If using an NVIDIA or AMD GPU, ensure you have enabled IOMMU in Proxmox and passed the PCIe device through to the VM.

## 2. Installing Ollama

Once your VM is provisioned and updated, install Ollama using the official automated script.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2.1 Verifying the Installation
After the script completes, verify that the Ollama service is active and running:

```bash
systemctl status ollama
```

## 3. Network Configuration for Remote Access

By default, Ollama binds to `127.0.0.1`, meaning it only accepts connections from within the VM itself. To allow access from your local network and Tailscale, you must modify the environment variables.

### 3.1 Binding to All Interfaces
Edit the Ollama service configuration to allow external connections:

```bash
sudo systemctl edit ollama.service
```

In the editor, add the following lines to the `[Service]` section:

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
Environment="OLLAMA_ORIGINS=*"
```

Save and exit, then reload the daemon and restart the service:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

### 3.2 Tailscale Integration
To access your AI models from outside your home network securely, install Tailscale on the VM:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Retrieve your VM's Tailscale IP address by running `tailscale ip -4`. Use this IP to connect your agents from any Tailscale-connected device.

## 4. Deploying Models and Connecting Agents

With the server configured, you can now download models and point your AI agents to the server's API.

### 4.1 Pulling Your First Model
Download a model (e.g., Llama 3) to verify everything is working:

```bash
ollama run llama3
```

### 4.2 Connecting AI Agents
AI agents (such as those built with AutoGen, LangChain, or CrewAI) require an API endpoint. Your Ollama API endpoint will be:

- **Local Network:** `http://<vm-local-ip>:11434`
- **Tailscale:** `http://<tailscale-ip>:11434`

Example connection test using `curl` from another device:

```bash
curl http://<your-ip>:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?"
}'
```

---
**Source:** [GitHub Issue #54](https://github.com/coltonchrane/AutoNotes/issues/54) | **Contributor:** @coltonchrane