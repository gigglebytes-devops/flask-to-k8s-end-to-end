# 🚀 Flask App Deployment with Docker & Kubernetes (No Host Required)

This project demonstrates how to **build and deploy** a simple Python **Flask** application using **Docker** and **Kubernetes**. The setup involves traffic routing via an **Ingress controller**, all configured locally — no custom domain name required!

---

## 📸 YouTube Tutorial

🎥 **Watch the full step-by-step tutorial here**  
👉 [Watch on YouTube](https://youtube.com/your-video-link)

---

## 📂 Project Structure

Here's a breakdown of the project files:

```plaintext
├── app.py                # Flask app code
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker configuration
├── k8s/                  # Kubernetes resources
│   ├── deployment.yaml   # Kubernetes deployment
│   ├── service.yaml      # Kubernetes service
│   └── ingress.yaml      # Kubernetes ingress
└── README.md             # Project documentation

🚀 Quick Start Guide
🔧 Prerequisites
Before starting, make sure you have the following:

Docker installed and configured

A Kubernetes cluster running locally (e.g., Minikube, Kind, docker desktop)

kubectl configured to access your cluster

Ingress Controller installed (e.g., NGINX)

🛠️ Steps to Deploy
Follow these steps to get your Flask app up and running on Kubernetes!

Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Build and Push the Docker Image

Build your Docker image and push it to Docker Hub:

bash
Copy
Edit
docker build -t yourdockerhubusername/flask-app:latest .
docker push yourdockerhubusername/flask-app:latest
Deploy to Kubernetes

Apply Kubernetes configurations to deploy the app:

bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
🧰 Tech Stack
Python 3.10 – Programming language for the Flask app

Flask – Lightweight Python web framework

Docker – Containerization tool for building and packaging the app

Kubernetes – Orchestrating the deployment and scaling

NGINX Ingress Controller – Managing incoming traffic to the app
