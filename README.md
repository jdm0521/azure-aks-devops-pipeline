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

* AKS uses **system-assigned managed identity**
* Secure image pulls from ACR using **RBAC (AcrPull role)**
* No credentials stored in code

---

## 🧠 Key Learnings

* Implemented Infrastructure as Code using Terraform
* Built CI/CD pipelines using GitHub Actions
* Deployed and managed containerized workloads in Kubernetes
* Debugged real-world issues with authentication, image pulls, and deployments
* Understood Kubernetes rollout behavior and image versioning

---

## 🎯 Project Highlights

* End-to-end DevOps pipeline (code → deployment)
* Fully automated container deployment
* Cloud-native architecture using AKS
* Secure service-to-service communication

---

## 🚀 Future Improvements

* 🔐 Azure Key Vault integration for secrets
* 📈 Horizontal Pod Autoscaler (HPA)
* 🌐 Ingress controller + custom domain
* 📊 Monitoring with Azure Monitor

---

## 👤 Author

Built as part of hands-on DevOps and cloud engineering practice.
