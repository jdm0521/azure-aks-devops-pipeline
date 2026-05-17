# 🚀 Azure DevOps AKS Microservices Deployment Pipeline

## 📌 Overview

This project demonstrates a complete end-to-end DevOps workflow by deploying a containerized Python API to Azure Kubernetes Service (AKS) using Infrastructure as Code and CI/CD automation.

It showcases how modern cloud-native applications are built, packaged, deployed, and managed in a scalable and secure environment.

---

## 🧩 Architecture

```
Developer Push (GitHub)
        ↓
GitHub Actions (CI/CD Pipeline)
        ↓
Docker Image Build
        ↓
Azure Container Registry (ACR)
        ↓
Azure Kubernetes Service (AKS)
        ↓
Kubernetes Deployment (Pods)
        ↓
Secrets Store CSI Driver
        ↓
Azure Key Vault
        ↓
Managed Identity Authentication
        ↓
Azure Monitor + Log Analytics
        ↓
LoadBalancer Service
        ↓
Public API Endpoint
```

---

## 🧱 Tech Stack

* Python (FastAPI)
* Docker (Containerization)
* Kubernetes (AKS)
* Terraform (Infrastructure as Code)
* GitHub Actions (CI/CD)
* Azure Container Registry (ACR)

---

## ⚙️ CI/CD Workflow

On every push to `main`:

1. Code is checked out from GitHub
2. Docker image is built
3. Image is pushed to Azure Container Registry
4. AKS deployment is updated
5. Kubernetes performs a rolling update

---

## ☁️ Infrastructure (Terraform)

Provisioned resources:

* Azure Resource Group
* Azure Kubernetes Service (AKS)
* Azure Container Registry (ACR)

### Deploy Infrastructure

```bash
terraform init
terraform apply
```

### Destroy Infrastructure

```bash
terraform destroy
```

---

## 🐳 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐳 Run with Docker

```bash
docker build -t aks-api .
docker run -p 8000:8000 aks-api
```

---

## 🌐 API Endpoints

* `/health` → Health check
* `/hello` → Sample response
* `/version` → App version

---

## 🧪 Sample Output

```
GET /health

{
  "status": "ok"
}
```

---


## 🔐 Security

* AKS uses Azure Managed Identities for secure Azure service authentication
* Secrets are securely stored in Azure Key Vault
* Kubernetes retrieves secrets dynamically using the Secrets Store CSI Driver
* No credentials or secrets are stored in application code or Kubernetes manifests
* Secure image pulls from Azure Container Registry (ACR) using RBAC (AcrPull role)


---

---
## 📊 Monitoring & Observability

Azure Monitor and Log Analytics were integrated with AKS to provide:

* Container and pod telemetry
* CPU and memory metrics
* Kubernetes event monitoring
* Centralized log collection
* Operational visibility through Azure Monitor Insights and KQL queries

Example KQL query:

```kql
ContainerLog
| where ContainerName contains "aks-api"
| limit 50
```
---

## 🧠 Key Learnings

* Implemented Infrastructure as Code using Terraform
* Built CI/CD pipelines using GitHub Actions
* Deployed and managed containerized workloads in Kubernetes
* Integrated Azure Key Vault with AKS using Managed Identities and the Secrets Store CSI Driver
* Implemented centralized monitoring and observability using Azure Monitor and Log Analytics
* Debugged real-world Kubernetes issues involving authentication, image pulls, secret injection, and infrastructure recreation
* Understood Kubernetes rollout behavior, workload security, and cloud-native operational patterns


---

## 🎯 Project Highlights

* End-to-end DevOps pipeline (code → deployment)
* Fully automated container deployment
* Cloud-native architecture using AKS
* Secure service-to-service communication

---

## 🚀 Future Improvements

📈 Horizontal Pod Autoscaler (HPA)
🌐 Ingress controller + custom domain
🚨 Alerting and notification rules
📊 Grafana dashboards and advanced observability
🔄 GitOps deployment workflow

---

## 👤 Author

Built as part of hands-on DevOps and cloud engineering practice.
