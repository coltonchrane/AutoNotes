---
layout: default
title: VNC Viewer: A Comprehensive Guide
parent: Networking
nav_order: 6
---

# VNC Viewer: A Comprehensive Guide

VNC Viewer is a graphical desktop-sharing application that allows you to remotely control one computer from another using the Virtual Network Computing (VNC) protocol. This guide explains the fundamentals of VNC and provides step-by-step instructions on how to install and use the software.

## 1. What is VNC?

VNC (Virtual Network Computing) is based on the Remote Frame Buffer (RFB) protocol. It works by transmitting the keyboard and mouse events from your local computer to a remote server and receiving graphical screen updates in return.

### Key Concepts
- **VNC Server:** The software installed on the remote computer that shares its screen.
- **VNC Viewer (Client):** The software installed on your local machine used to view and interact with the remote desktop.
- **Platform Independence:** VNC is cross-platform, meaning you can connect from a Windows machine to a Linux server, or vice versa.

## 2. Installation

Depending on your operating system, there are several popular VNC Viewer clients available, such as RealVNC, TigerVNC, and TightVNC.

### Linux (Ubuntu/Debian)
You can install a common VNC viewer using the following command:
```bash
sudo apt update
sudo apt install xtightvncviewer
```

### macOS
macOS has a built-in client called 'Screen Sharing', but for more features, you can install RealVNC via Homebrew:
```bash
brew install --cask vnc-viewer
```

### Windows
The most common method is downloading the standalone installer from [RealVNC](https://www.realvnc.com/en/connect/download/viewer/). Alternatively, using Chocolatey:
```powershell
choco install vnc-viewer
```

## 3. How to Use VNC Viewer

To connect to a remote computer, the VNC Server must already be running on the target machine.

### Establishing a Connection
1. **Launch the Application:** Open VNC Viewer on your local machine.
2. **Enter the Address:** In the connection bar, enter the IP address or hostname followed by the display number or port.
   - *Example:* `192.168.1.50:1` or `192.168.1.50:5901`
3. **Authentication:** Click 'Connect'. You will typically be prompted for a password that was configured on the VNC Server.
4. **Session Control:** Once authenticated, the remote desktop will appear in a window. You can now use your mouse and keyboard as if you were sitting in front of the remote machine.

## 4. Configuration and Optimization

### Connection Settings
Inside VNC Viewer, you can modify settings to improve performance based on your network speed:
- **Picture Quality:** Set to 'Low' or 'Medium' if you are experiencing lag over a slow internet connection.
- **Scaling:** Choose 'Scale to fit window' to ensure the remote desktop fits your local screen size.

### Common Ports
- **Default Port:** 5900
- **Display :1:** 5901
- **Display :2:** 5902

## 5. Security Best Practices

Basic VNC traffic is often unencrypted. To protect your data and credentials, follow these security steps:

### Use an SSH Tunnel
Encapsulate your VNC traffic within an encrypted SSH connection by running this command on your local machine:
```bash
ssh -L 5901:localhost:5901 user@remote-server-ip
```
After running this, connect your VNC Viewer to `localhost:5901` instead of the remote IP directly.

---
**Source:** [GitHub Issue #60](https://github.com/coltonchrane/AutoNotes/issues/60) | **Contributor:** @coltonchrane