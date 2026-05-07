---
layout: default
title: Hosting Websites on Google Ecosystem
parent: Cloud Computing
nav_order: 1
---

# Hosting Websites on Google Ecosystem

Google Cloud Platform (GCP) and Firebase offer several robust methods for hosting websites, ranging from simple static pages to complex, auto-scaling web applications. This guide provides an overview of the four primary hosting solutions available within the Google ecosystem.

## 1. Google Cloud Storage (Static Website Hosting)

Google Cloud Storage (GCS) is the most cost-effective solution for hosting static websites that consist only of client-side files like HTML, CSS, JavaScript, and images.

### 1.1 Key Features
- Extremely low cost for small to medium sites.
- High availability and durability.
- Integration with Cloud CDN for global performance.

### 1.2 Configuration Example
After creating a bucket named after your domain, you can set the default index and error pages using the `gsutil` tool:

```bash
# Set index.html and 404.html for the bucket
gsutil web set -m index.html -e 404.html gs://www.your-domain.com

# Make the objects publicly readable
gsutil iam ch allUsers:objectViewer gs://www.your-domain.com
```

## 2. Firebase Hosting (Modern Web Apps)

Firebase Hosting is designed for modern web developers. It is ideal for Single Page Applications (SPAs) and provides premium features like free SSL and a global CDN by default.

### 2.1 Initialization
You must first install the Firebase CLI and login to your account:

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
```

### 2.2 Deployment
Once your project is initialized and your files are in the public directory, deployment is a single command:

```bash
firebase deploy
```

## 3. Google App Engine (PaaS)

App Engine is a Platform-as-a-Service (PaaS) that allows you to build and deploy applications in a serverless environment. It supports various languages including Node.js, Python, Java, and Go.

### 3.1 App Configuration
You define your environment in an `app.yaml` file:

```yaml
runtime: nodejs18
instance_class: F1
handlers:
- url: /.*
  script: auto
```

### 3.2 Deployment
Deploy your app directly to Google Cloud using the SDK:

```bash
gcloud app deploy
```

## 4. Google Compute Engine (IaaS)

For users requiring full control over the operating system, Compute Engine provides Virtual Machines (VMs). This is necessary if you need to install specific software or custom server configurations (e.g., Nginx, Apache, or Docker).

### 4.1 Setup Example (Nginx on Ubuntu)
After creating your VM instance in the Google Cloud Console, you can install a web server via SSH:

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
```

### 4.2 Firewall Rules
Ensure that HTTP (port 80) and HTTPS (port 443) traffic are allowed in your VPC firewall settings to make the website accessible to the public.

---
**Source:** [GitHub Issue #64](https://github.com/coltonchrane/AutoNotes/issues/64) | **Contributor:** @coltonchrane