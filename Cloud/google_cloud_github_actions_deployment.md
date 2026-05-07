---
layout: default
title: Deploying to Google Cloud Platform using GitHub Actions
parent: Cloud
nav_order: 1
---

# Deploying to Google Cloud Platform using GitHub Actions

This guide provides a comprehensive walkthrough for automating the deployment of applications and websites to Google Cloud Platform (GCP) using GitHub Actions workflows. By leveraging modern authentication methods like Workload Identity Federation, you can create secure and efficient CI/CD pipelines.

## 1. Prerequisites

Before configuring the automation, ensure you have the following components ready:

- A **Google Cloud Project** with billing enabled.
- The **Google Cloud CLI** installed locally for initial configuration.
- A **GitHub Repository** containing your application source code.
- Necessary APIs enabled in your GCP project (e.g., Cloud Run API, Artifact Registry API, or Cloud Storage API).

## 2. Setting Up Secure Authentication

It is highly recommended to use **Workload Identity Federation** instead of long-lived Service Account keys. This allows GitHub Actions to impersonate a service account using short-lived tokens.

### 2.1 Create a Service Account
First, create a service account that GitHub Actions will use to perform deployments.

```bash
gcloud iam service-accounts create "github-actions-deployer" \
    --display-name="GitHub Actions Deployer"
```

### 2.2 Configure Workload Identity Federation
Create a workload identity pool and provider to establish trust between GitHub and GCP.

```bash
# Create the pool
gcloud iam workload-identity-pools create "github-pool" \
    --location="global" --display-name="GitHub Pool"

# Create the provider
gcloud iam workload-identity-pools providers create-oidc "github-provider" \
    --location="global" \
    --workload-identity-pool="github-pool" \
    --issuer-uri="https://token.actions.githubusercontent.com" \
    --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository"
```

## 3. Configuring GitHub Repository Secrets

Navigate to your GitHub repository settings and add the following as **Actions Secrets**:

- `GCP_PROJECT_ID`: Your unique Google Cloud Project ID.
- `GCP_SERVICE_ACCOUNT`: The email of the service account created in step 2.1.
- `GCP_WORKLOAD_IDENTITY_PROVIDER`: The full identifier of the provider (e.g., `projects/123456789/locations/global/workloadIdentityPools/github-pool/providers/github-provider`).

## 4. Creating the Deployment Workflow

Create a file at `.github/workflows/deploy.yml` in your repository. The following example demonstrates a deployment to **Google Cloud Run**.

### 4.1 Workflow Configuration Example

```yaml
name: Deploy to Google Cloud

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: 'read'
      id-token: 'write'

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Authenticate to Google Cloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Build and Deploy to Cloud Run
        run: |
          gcloud builds submit --tag gcr.io/${{ secrets.GCP_PROJECT_ID }}/my-app
          gcloud run deploy my-app \
            --image gcr.io/${{ secrets.GCP_PROJECT_ID }}/my-app \
            --region us-central1 \
            --platform managed \
            --allow-unauthenticated
```

## 5. Deploying Static Sites to Cloud Storage

If you are deploying a static website (HTML/CSS/JS) to a Google Cloud Storage bucket, replace the deployment step in the workflow above with the following snippet:

```yaml
      - name: Upload to Cloud Storage
        run: |
          gsutil -m cp -r ./dist/* gs://your-bucket-name/
```

---
**Source:** [GitHub Issue #66](https://github.com/coltonchrane/AutoNotes/issues/66) | **Contributor:** @coltonchrane