---
layout: default
title: Creating and Flashing a Custom Ubuntu Image
parent: Linux
nav_order: 4
---

# Creating and Flashing a Custom Ubuntu Image

This guide explains how to create a customized Ubuntu ISO pre-loaded with your favorite applications and configurations. This process eliminates the need to manually download and install software every time you perform a fresh installation on a new machine.

## 1. Overview of Customization Tools

To create a custom Ubuntu image, we use a tool called **Cubic** (Custom Ubuntu ISO Creator). Cubic provides a GUI-based wizard and a chroot environment that allows you to modify the file system of an existing ISO.

## 2. Installation and Setup

Before you begin, you need a host machine running Ubuntu and the official ISO file you intend to customize.

### Installing Cubic
Add the official PPA and install the package using the following commands:

```bash
sudo add-apt-repository ppa:cubic-wizard/release
sudo apt update
sudo apt install cubic
```

## 3. Creating the Custom ISO

### Initial Configuration
1. Launch **Cubic** from your application menu.
2. Select a new directory to serve as your project workspace.
3. Select the source ISO (the official Ubuntu image you downloaded).
4. Set the custom ISO parameters, such as the volume ID and release name.

### Modifying the System (Chroot)
Cubic will extract the compressed file system and open a terminal. Any command you run here affects the custom image, not your host system.

Use this environment to install the apps you want to be available by default:

```bash
# Update the package lists
apt update

# Install your required applications
apt install -y vlc git curl gnome-tweaks build-essential

# Remove unnecessary packages to save space
apt autoremove --purge
```

### Finalizing the Build
Once you have finished installing your applications:
1. Click **Next** to select the kernel version and boot configurations.
2. Choose the packages you wish to remove (if using the "Minimal Install" option).
3. Click **Generate** to create the final `.iso` file.

## 4. Flashing the Image to a USB Drive

After Cubic generates your custom ISO, you need to write it to a physical flash drive. 

### Using the Command Line (dd tool)
Identify your USB drive path (e.g., `/dev/sdb`) using `lsblk`, then run the following command. **Warning:** This will erase all data on the target drive.

```bash
# Replace 'custom-ubuntu.iso' with your filename and '/dev/sdX' with your USB device
sudo dd if=custom-ubuntu.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

### Using a GUI Tool
If you prefer a graphical interface, you can use **BalenaEtcher** or the **Startup Disk Creator** tool included in Ubuntu to select your custom ISO and flash it to your USB drive.

---
**Source:** [GitHub Issue #49](https://github.com/coltonchrane/AutoNotes/issues/49) | **Contributor:** @coltonchrane