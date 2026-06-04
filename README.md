ACME-Streamly Cloud Native Application

This project transforms a legacy monolithic application into a three-tier cloud-native application using Docker, Kubernetes and modern cloud-native technologies.

Technologies Used:

* Docker
* Docker Compose
* Kubernetes
* Minikube
* PostgreSQL
* Prometheus
* Grafana
* OpenFaaS
* K3s Edge Computing

**Architecture**

Frontend
|
Backend API
|
PostgreSQL Database

**Prequisits**

All the following technologies must be installed locally:

Docker Desktop
Minikube
kubectl
Helm
OpenFaaS CLI

** Clone repository and deploy images***

git clone <repository>

cd app

Start the docker engine by opening the app, then:

docker build -t frontend:latest ./web

docker build -t backend:latest ./backend

**Verify**

docker images

**Expected outcome**

You can see the images there

**Start Kubernetes Cluster**

minikube start

**Verify**

minikube status

**Expected Outcome**

The Kubernetes cluster should be running correctly.

**Apply all kubernetes manifests files**

kubectl apply -f k8s/

**Verify**

kubectl get pods

kubectl get services

kubectl get deployments

**Expected Outcome**

All resources that were verified should appear with those commands as specified in the manifest files (amount of replicas and state should be running if applicable).

**Access Application**

minikube service frontend-service

**Expected Outcome**

The application should open in the browser and communication between frontend, backend and database should be operational.

**Monitoring Stack**

helm install monitoring prometheus-community/kube-prometheus-stack

**Verify**

kubectl get pods

**Expected Outcome**

Prometheus and Grafana pods should be running.

**OpenFaaS**

kubectl port-forward -n openfaas svc/gateway 8080:8080

**Verify**

faas-cli list

**Expected Outcome**

The deployed function should appear in the OpenFaaS gateway.
