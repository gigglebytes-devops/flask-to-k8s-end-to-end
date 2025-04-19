# flask-to-k8s-end-to-end

# 🐍 Flask App Deployment with Docker & Kubernetes (No Host Required)

This project shows how to build and deploy a simple Python Flask application using **Docker** and **Kubernetes**, with traffic routing via an **Ingress controller** — all set up locally and without needing a custom domain name.

---

## 📸 YouTube Tutorial

🎥 **Watch the full step-by-step tutorial here**  
👉 [YouTube Video Link](https://youtube.com/your-video-link)

---

## 📁 Project Structure

├── app.py                # Flask app
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── README.md


---

## 🚀 Quick Start Guide

### 🔧 Prerequisites

- Docker installed and configured
- Kubernetes cluster running locally (e.g. Minikube, Kind)
- kubectl configured to access your cluster
- Ingress Controller installed (e.g. NGINX)

> 💡 If using Minikube, enable ingress:  
> `minikube addons enable ingress`

---

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### 1. Clone the Repository

docker build -t yourdockerhubusername/flask-app:latest .
docker push yourdockerhubusername/flask-app:latest
