# 🚀 Cloud-Native CI/CD Pipeline using Docker & Kubernetes on AWS

## 📌 Project Overview
This project focuses on designing and implementing a Cloud-Native Continuous Integration and Continuous Deployment (CI/CD) pipeline for deploying containerized applications using Docker and Kubernetes on AWS. The main objective is to automate the software deployment process and reduce manual intervention.

The pipeline automatically builds, containerizes, and deploys the application whenever new code is pushed to the GitHub repository. The application is deployed on a Kubernetes cluster hosted on AWS cloud infrastructure. Monitoring tools like Prometheus and Grafana are used to monitor application performance and system metrics.

---

## ⚙️ Tools & Technologies Used
- GitHub (Source Code Management)
- GitHub Actions (CI/CD Pipeline)
- Docker (Containerization)
- Kubernetes (Container Orchestration)
- AWS EC2 (Cloud Infrastructure)
- AWS ECR (Container Registry)
- Prometheus (Monitoring)
- Grafana (Visualization Dashboard)
- Linux (Operating System)

---

## 🔄 Project Workflow
1. Developer pushes code to GitHub repository
2. CI/CD pipeline is triggered automatically
3. Application Docker image is built
4. Docker image is pushed to AWS Elastic Container Registry (ECR)
5. Kubernetes cluster pulls the image from ECR
6. Application is deployed on Kubernetes
7. Prometheus collects metrics and system data
8. Grafana displays monitoring dashboards

---

## ✨ Key Features
- Automated CI/CD pipeline
- Docker containerization
- Kubernetes deployment
- AWS cloud deployment
- Infrastructure automation
- Real-time monitoring using Prometheus and Grafana
- Scalable and reliable deployment process

---

## 📁 Project Structure
project/
│
├── app/
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── README.md

---

## 🎯 Project Outcome
Successfully implemented a Cloud-Native CI/CD pipeline that automates application build, containerization, and deployment using Docker, Kubernetes, and AWS with monitoring support using Prometheus and Grafana.

This project demonstrates practical implementation of DevOps tools and cloud technologies used in real-world industry environments.

---

## 👩‍💻 Author
Mamta Gupta
DevOps Project
