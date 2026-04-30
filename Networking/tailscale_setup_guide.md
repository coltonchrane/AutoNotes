---
layout: default
title: How to Download, Run, and Configure Tailscale
parent: Networking
nav_order: 5
---

# How to Download, Run, and Configure Tailscale

Tailscale is a zero-config VPN that creates a secure mesh network between your devices using the WireGuard protocol. This guide provides a step-by-step walkthrough for installing, authenticating, and managing Tailscale specifically on Ubuntu and other Linux-based distributions.

## 1. Installation on Ubuntu/Linux

Tailscale provides an automated script for most Linux distributions, but you can also install it manually via the package manager for better version control on Ubuntu.

### Automated Installation (Recommended)
The most efficient way to install Tailscale is using the official one-line script, which detects your distribution, adds the Tailscale repository, and installs the package automatically.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### Manual Installation (APT Repository)
If you prefer to manage the repository manually on Ubuntu, follow these steps to add the official Tailscale repository:

1. **Add Tailscale’s GPG key:**
   ```bash
   sudo mkdir -p --mode=0755 /usr/share/keyrings
   curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/$(lsb_release -cs).noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
   ```

2. **Add the repository to your sources list:**
   ```bash
   curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/$(lsb_release -cs).tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list
   ```

3. **Install the Tailscale client:**
   ```bash
   sudo apt update && sudo apt install tailscale
   ```

## 2. Running and Authenticating

On Linux, Tailscale runs as a system daemon (`tailscaled`). Once installed, the service usually starts automatically, but you must manually authenticate the device to link it to your Tailnet.

### Managing the Service
Ensure the daemon is enabled and running using `systemd`:
```bash
sudo systemctl enable --now tailscaled
```

### Connecting to Existing Infrastructure
When you run the `up` command, you are effectively joining your machine to an existing Tailnet (your private network). 

**Standard Authentication:**
To bring the interface up and link the machine via a web browser:
```bash
sudo tailscale up
```
Copy the generated URL into a browser and sign in using your existing SSO provider (Google, Microsoft, GitHub, etc.) to register the device.

**Headless/Automated Authentication (Auth Keys):**
If you are connecting a server to an existing infrastructure without access to a web browser, use a pre-authenticated auth key generated from the [Tailscale Admin Console](https://login.tailscale.com/admin/settings/keys):
```bash
sudo tailscale up --authkey=tskey-auth-kXXXXX-XXXXXXXXXXXXXXXX
```

**Connecting to a Private Coordination Server (Headscale):**
If your infrastructure uses [Headscale](https://github.com/juanfont/headscale) (an open-source, self-hosted implementation of the Tailscale control server), point your client to your specific login URL:
```bash
sudo tailscale up --login-server https://headscale.example.com
```

## 3. Configuration and Advanced Features

Tailscale offers powerful features optimized for Linux servers and workstations, manageable directly from the command line.

### Setting Up an Exit Node
If you want to route internet traffic from other devices through this Ubuntu machine (useful for secure browsing on public Wi-Fi), configure it as an exit node:
```bash
sudo tailscale up --advertise-exit-node
```
*Note: You may need to enable IP forwarding in `/etc/sysctl.conf` for this feature to function.*

### Enabling Tailscale SSH
Tailscale can manage SSH authentication for you, allowing you to access your Linux machine without manual SSH key management:
```bash
sudo tailscale up --ssh
```

### Advertising Subnet Routes
To allow Tailscale to access other devices on your local physical network (e.g., `192.168.1.0/24`), use the `--advertise-routes` flag:
```bash
sudo tailscale up --advertise-routes=192.168.1.0/24
```

## 4. Managing the Network

### Checking Connection Status
To view all devices currently connected to your Tailnet and their respective IP addresses:
```bash
tailscale status
```

### Finding Your Local Tailscale IP
To quickly retrieve only the IPv4 address assigned to your machine:
```bash
tailscale ip -4
```

### Disconnecting and Stopping
To disconnect from the Tailnet without uninstalling the software:
```bash
sudo tailscale down
```

To fully stop the background process:
```bash
sudo systemctl stop tailscaled
```

---
**Source:** [GitHub Issue #51](https://github.com/coltonchrane/AutoNotes/issues/51) | **Contributor:** @coltonchrane
---