# ACME-Streamly Cloud Native Application

A three-tier cloud-native application developed as part of my BSc Cyber Security coursework.

The project involved containerising and deploying a frontend, backend API and PostgreSQL database using Docker and Kubernetes, with Kubernetes security controls, monitoring and edge/serverless technologies.

## Technologies Used

- Docker
- Docker Compose
- Kubernetes
- Minikube
- PostgreSQL
- Prometheus
- Grafana
- OpenFaaS
- K3s
- Helm

## Architecture

```text
Frontend
   |
Backend API
   |
PostgreSQL Database
```

## Security

The Kubernetes deployment includes security controls such as:

- Kubernetes Secrets for sensitive database configuration
- NetworkPolicies restricting communication between application tiers
- Separation of frontend, backend and database workloads
- ClusterIP exposure for the database to avoid unnecessary external access

## Prerequisites

The following technologies must be installed locally:

- Docker Desktop
- Minikube
- kubectl
- Helm
- OpenFaaS CLI

## Clone Repository and Build Images

```bash
git clone https://github.com/ismailbutthaleem/kubernetes-cloud-security-lab
cd kubernetes-cloud-security-lab
```

Start Docker Desktop, then:

```bash
docker build -t frontend:latest ./web
docker build -t backend:latest ./backend
```

### Verify

```bash
docker images
```

**Expected outcome:** The frontend and backend images should appear in the image list.

## Start Kubernetes Cluster

```bash
minikube start
```

### Verify

```bash
minikube status
```

**Expected outcome:** The Kubernetes cluster should be running correctly.

## Deploy to Kubernetes

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

### Verify

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
```

**Expected outcome:** The Kubernetes resources should appear as defined in the manifest files, with the required replicas running.

## Access the Application

```bash
minikube service frontend-service
```

**Expected outcome:** The application should open in the browser and communication between the frontend, backend and database should be operational.

## Monitoring Stack

Install the Prometheus and Grafana monitoring stack:

```bash
helm install monitoring prometheus-community/kube-prometheus-stack
```

### Verify

```bash
kubectl get pods
```

**Expected outcome:** Prometheus and Grafana pods should be running.

## OpenFaaS

Forward the OpenFaaS gateway:

```bash
kubectl port-forward -n openfaas svc/gateway 8080:8080
```

### Verify

```bash
faas-cli list
kubectl get pods -n openfaas
```

**Expected outcome:** The deployed function should appear in the OpenFaaS gateway.

## Documentation

The development process, implementation decisions and troubleshooting carried out throughout the project are documented in [`Technical_Logbook.md`](Technical_Logbook.md).

## Project Context

This project was completed as part of my BSc Cyber Security coursework and was developed and tested within a local lab environment.
