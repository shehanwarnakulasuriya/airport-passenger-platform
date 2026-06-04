# Airport Passenger Processing Platform Architecture

## Overview

The Airport Passenger Processing Platform is a cloud-native three-tier application designed to demonstrate Platform Engineering, Kubernetes, Observability, DevOps, and Solution Architecture concepts.

The solution consists of:

- React Frontend
- Nginx Reverse Proxy
- Python Flask Backend API
- PostgreSQL Database
- Docker Containerization
- Kubernetes Orchestration
- GitHub Actions Continuous Integration (CI)
- Prometheus Monitoring
- Grafana Dashboards

---

# Architecture Diagram

> Detailed end-to-end architecture

![Airport Passenger Platform Architecture](screenshots/architecture.png)

---

# Business Objective

The application simulates an airport passenger processing platform allowing users to:

- View passenger records
- Retrieve passenger details
- Perform passenger check-in operations
- Monitor platform health and performance

---

# Current State Architecture

The current implementation demonstrates:

- Local Kubernetes development using Minikube
- Containerized application workloads
- Continuous Integration (CI)
- Observability
- Service-to-service communication
- Persistent data storage

Deployment remains local and manual.

GitHub Actions currently performs build validation only.

---

# Developer Workflow

```text
Developer Workstation
        ↓
Git Commit
        ↓
GitHub Repository
        ↓
GitHub Actions CI
        ↓
Docker Build Validation
```

### Components

- VS Code
- Git
- GitHub
- Docker CLI

Responsibilities:

- Source code management
- Build validation
- Repository documentation

---

# Continuous Integration (CI)

GitHub Actions provides Continuous Integration.

Pipeline activities:

- Source checkout
- Backend Docker image build
- Frontend Docker image build
- Build validation

Workflow:

```text
Developer
    ↓
Git Push
    ↓
GitHub Actions
    ↓
Backend Build
    ↓
Frontend Build
    ↓
Pass / Fail
```

Current implementation:

✅ CI Implemented

❌ CD Not Implemented

---

# Containerization Layer

The application is packaged into two Docker images:

```text
backend-api:v1
frontend:v1
```

Build flow:

```text
Source Code
      ↓
Docker Build
      ↓
Docker Images
      ↓
Minikube Image Store
```

Benefits:

- Portability
- Repeatability
- Environment consistency

---

# Kubernetes Platform

The platform runs on:

```text
Minikube Kubernetes Cluster
```

Application namespace:

```text
airport-platform
```

Monitoring namespace:

```text
monitoring
```

---

# Frontend Layer

## Technology

- React
- Vite
- Nginx

## Kubernetes Resources

- frontend Deployment
- frontend-service NodePort Service

## Responsibilities

- Display passenger information
- Trigger passenger check-in actions
- Consume backend APIs

Request flow:

```text
Browser
    ↓
frontend-service
    ↓
Frontend Pods
```

---

# Nginx Reverse Proxy

Nginx performs two functions:

## Static Content Hosting

Serves:

- React build files
- JavaScript
- CSS
- HTML

## API Proxy

Routes:

```text
/api/*
```

to:

```text
backend-service
```

Example:

```text
/api/passengers
       ↓
backend-service
       ↓
Flask API
```

Benefits:

- Single application entry point
- Simplified frontend configuration
- Reduced browser CORS complexity

---

# Backend Layer

## Technology

- Python Flask
- Flask-CORS
- Prometheus Flask Exporter

## Kubernetes Resources

- backend-api Deployment
- backend-service ClusterIP Service

## API Endpoints

```text
GET  /health
GET  /passengers
GET  /passengers/{id}
POST /checkin/{id}
GET  /metrics
```

## Responsibilities

- Business logic execution
- Passenger retrieval
- Passenger updates
- Database connectivity
- Metrics generation

---

# Configuration Management

Application configuration is externalized using Kubernetes resources.

## ConfigMap

Stores non-sensitive configuration:

```text
APP_ENV
APP_VERSION
DB_HOST
DB_NAME
DB_PORT
```

## Secret

Stores sensitive values:

```text
DB_USER
DB_PASSWORD
API_KEY
```

Benefits:

- Environment portability
- Separation of configuration from code
- Improved security

---

# Database Layer

## Technology

- PostgreSQL 16

## Kubernetes Resources

- postgres Deployment
- postgres-service ClusterIP Service

Database:

```text
passengerdb
```

Table:

```text
passengers
```

Responsibilities:

- Passenger data storage
- Check-in status persistence

---

# Persistent Storage

The database uses:

```text
PersistentVolumeClaim
```

Resource:

```text
postgres-pvc
```

Storage:

```text
1Gi
```

Benefits:

```text
Pod Restart
      ↓
Data Preserved
```

instead of:

```text
Pod Restart
      ↓
Data Lost
```

---

# Service Discovery

Kubernetes Services provide internal networking.

Frontend:

```text
frontend-service
```

Backend:

```text
backend-service
```

Database:

```text
postgres-service
```

The backend connects to PostgreSQL using:

```text
DB_HOST=postgres-service
```

which is automatically resolved through Kubernetes DNS.

---

# Observability Architecture

Monitoring resources are deployed into:

```text
monitoring
```

namespace.

Components:

- Prometheus
- Grafana
- AlertManager

---

## Prometheus

Responsibilities:

- Collect application metrics
- Collect Kubernetes metrics
- Store time-series data

Metrics include:

- Request count
- Request rate
- Response latency
- CPU utilization
- Memory utilization
- Pod restarts

---

## ServiceMonitor

Prometheus discovers backend metrics through:

```text
backend-api-monitor
```

Scrape target:

```text
/metrics
```

Scrape interval:

```text
15 seconds
```

---

## Grafana

Grafana visualizes platform metrics.

Dashboard panels:

- Backend Request Count
- Backend Request Rate
- Backend Latency
- Pod CPU Usage
- Pod Memory Usage
- Pod Restarts
- PostgreSQL Health

---

# End-to-End Request Flow

## Passenger Retrieval

```text
Browser
    ↓
frontend-service
    ↓
Frontend Pod
    ↓
Nginx
    ↓
backend-service
    ↓
Flask API
    ↓
postgres-service
    ↓
PostgreSQL
```

---

## Passenger Check-In

```text
Browser
    ↓
Check-In Button
    ↓
POST /checkin/P1002
    ↓
Flask API
    ↓
PostgreSQL Update
    ↓
Response Returned
```

---

# Future State Architecture

The future state extends the platform from CI to full CI/CD and cloud deployment.

Planned enhancements:

- GitHub Actions CI/CD
- Container Registry (ECR/ACR)
- Terraform Infrastructure as Code
- AWS EKS or Azure AKS
- Managed PostgreSQL
- Kubernetes Ingress
- AlertManager Notifications
- Horizontal Pod Autoscaling
- Centralized Logging

Future workflow:

```text
Developer
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Docker Build
    ↓
Security Scan
    ↓
Container Registry
    ↓
Terraform
    ↓
EKS / AKS
    ↓
Automated Deployment
```

---

# Key Concepts Demonstrated

- Solution Architecture
- Platform Engineering
- Docker
- Kubernetes
- Service Discovery
- Configuration Management
- Persistent Storage
- Observability
- Monitoring
- Continuous Integration
- Cloud-Native Design

---

# Author

Shehan Warnakulasuriya

Senior Systems Analyst Specialist  
Solution Design  
AWS Certified Solutions Architect  
Cloud & Platform Engineering