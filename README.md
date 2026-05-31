# Airport Passenger Processing Platform

A cloud-native three-tier application demonstrating modern platform engineering, Kubernetes, observability, and DevOps practices.

This project simulates an airport passenger processing platform where users can view passenger information and perform passenger check-in operations through a web interface.

---

## Architecture Overview

The platform consists of three application layers deployed on Kubernetes:

```text
Browser
   │
   ▼
Frontend (React + Nginx)
   │
   ▼
Backend API (Python Flask)
   │
   ▼
PostgreSQL Database
```

Observability Layer:

```text
Prometheus
   │
   ▼
Backend Metrics (/metrics)

Grafana
   │
   ▼
Dashboards & Monitoring
```

---

## Technology Stack

### Frontend

- React
- Vite
- Nginx

### Backend

- Python
- Flask
- Flask-CORS
- Prometheus Flask Exporter

### Database

- PostgreSQL

### Platform

- Docker
- Kubernetes
- Minikube

### DevOps

- Git
- GitHub
- GitHub Actions

### Observability

- Prometheus
- Grafana

---

## Key Features

### Passenger Management

- View passenger records
- Passenger check-in workflow
- REST API integration

### Kubernetes Platform Features

- Deployments
- Services
- ConfigMaps
- Secrets
- PersistentVolumeClaims
- Health Probes
- Scaling

### Observability

- Application Metrics
- Prometheus Scraping
- Grafana Dashboards
- Health Endpoints
- Operational Monitoring

---

## Project Structure

```text
airport-passenger-platform/
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── nginx.conf
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── backend-servicemonitor.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
│
├── docs/
│   ├── architecture.md
│   └── screenshots/
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Skills Demonstrated

This project demonstrates practical experience in:

### Solution Design

- Three-tier architecture
- Service-to-service communication
- API design patterns
- Architectural documentation

### Platform Engineering

- Kubernetes workload management
- Configuration management
- Secrets management
- Persistent storage

### DevOps

- Docker image creation
- CI validation pipelines
- Git workflows
- Deployment automation

### Reliability Engineering

- Liveness probes
- Readiness probes
- Operational troubleshooting
- Scaling workloads

### Observability

- Metrics collection
- Application monitoring
- Dashboard creation
- Operational visibility

---

## Architecture Decisions

### Why Kubernetes?

Kubernetes provides:

- Automated deployment
- Service discovery
- Scaling
- Health monitoring
- Declarative infrastructure

### Why PostgreSQL?

PostgreSQL provides:

- Reliable persistence
- ACID compliance
- Relational data modelling

### Why Prometheus and Grafana?

Prometheus and Grafana provide:

- Real-time metrics
- Operational visibility
- Capacity monitoring
- Performance insights

---

## Local Development

### Start Minikube

```bash
minikube start --driver=docker
```

### Deploy Platform

```bash
kubectl apply -f k8s/
```

### Verify Resources

```bash
kubectl get all -n airport-platform
```

### Access Frontend

```bash
minikube service frontend-service -n airport-platform
```

---

## Monitoring

### Backend Metrics

```bash
curl http://localhost:5000/metrics
```

### Access Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

Open:

```text
http://localhost:3000
```

---

## Screenshots

Add screenshots showing:

- Kubernetes Deployments
- Running Pods
- Passenger Processing UI
- GitHub Actions Pipeline
- Prometheus Targets
- Grafana Dashboards

---

## Future Enhancements

- Kubernetes Ingress
- Helm Charts
- Terraform
- Azure AKS Deployment
- AWS EKS Deployment
- Horizontal Pod Autoscaling
- Alerting & Notifications
- Centralised Logging

---

## Learning Outcomes

Through this project I developed hands-on experience with:

- Kubernetes
- Platform Engineering
- Cloud-Native Architecture
- DevOps Practices
- Observability
- Reliability Engineering
- Solution Architecture

---

## Author

Shehan Warnakulasuriya

Senior Systems Analyst Specialist | Solution Design | AWS Certified Solutions Architect | Cloud & Platform Engineering