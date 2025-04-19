# 🚀 Flask App Deployment with Docker & Kubernetes (No Host Required)

This project demonstrates how to **build and deploy** a simple Python **Flask** application using **Docker** and **Kubernetes**. The setup includes traffic routing via an **Ingress controller**, configured locally without requiring a custom domain!

[![YouTube Tutorial](https://youtu.be/wlTXpMNPi-g)

---

## 📂 Project Structure

```plaintext
├── app.py                # Flask application code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build configuration
├── k8s/                  # Kubernetes manifests
│   ├── deployment.yaml   # App deployment configuration
│   ├── service.yaml      # Network service definition
│   └── ingress.yaml      # Traffic routing rules
└── README.md             # Project documentation

🚀 Quick Start Guide
🔧 Prerequisites
Docker installed & running

Kubernetes cluster (Minikube, Kind, or Docker Desktop)

kubectl configured for cluster access

Ingress controller (NGINX recommended)

🛠️ Deployment Steps
Clone Repository

bash
git clone https://github.com/gigglebytes-devops/flask-to-k8s-end-to-end.git
cd flask-to-k8s-end-to-end

Build & Push Docker Image:

docker build -t yourdockerhubusername/flask-app:latest .
docker push yourdockerhubusername/flask-app:latest

Deploy Kubernetes Resources:

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml


🌐 Accessing the Application
After deployment completes:

Get the ingress IP address:

kubectl get ingress -n <namespace>


🧰 Tech Stack
Python 3.10 - Core programming language

Flask - Micro web framework

Docker - Containerization platform

Kubernetes - Container orchestration

NGINX Ingress - Traffic management

