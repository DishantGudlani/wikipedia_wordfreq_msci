#Timestamp Service – Kubernetes Assignment
This project implements a simple timestamp service in Go, packages it into a Docker image, and deploys it to a local Kubernetes cluster using Minikube. The service exposes two HTTP endpoints:
POST /timestamp — accepts a Unix timestamp in the request body
GET /timestamp — returns the most recently stored timestamp
The assignment demonstrates containerization, Kubernetes deployments, and basic service exposure.

#Project Structure
.
├── main.go
├── main_test.go
├── Dockerfile
└── k8s.yaml

#How the Application Works
The server starts and exposes two endpoints on port 8080.
The client sends a POST request with the current Unix timestamp.
The server stores the timestamp in memory.
The client sends a GET request to retrieve it.
The program prints the timestamp and exits.
Because the program exits after running the client, the Kubernetes pod will show:
```bash
STATUS: Completed
```
This is expected behavior.

##Build and Run Locally
Run tests
```bash
go test ./...
```
Build the binary
```bash
go build -o app main.go
```
Run the app
```bash
./app
```

##Docker Instructions
Build the Docker image
```bash
docker build -t timestamp-service:latest .
```

Run the container
```bash
docker run --rm -p 8080:8080 timestamp-service:latest
```

##Kubernetes Deployment (Minikube)
1. Start Minikube
```bash
minikube start
```
2. Load the Docker image into Minikube
```bash
minikube image load timestamp-service:latest
```
3. Apply the Kubernetes manifest
```bash
kubectl apply -f k8s.yaml
```
4. (Optional) Restart the pod
```bash
kubectl delete pod -l app=timestamp-service
```
5. Check pod status
```bash
kubectl get pods
```

Expected:
```bash
0/1   Completed
```
6. View logs
```bash
kubectl logs deployment/timestamp-service
```
You should see a Unix timestamp printed.

Kubernetes Manifest
The deployment uses:
```bash
imagePullPolicy: Never
```

Ensures Kubernetes uses the local Minikube image instead of pulling from Docker Hub.
A simple ClusterIP service exposing port 80 → 8080.

##Endpoints
Once port-forwarded or exposed:
POST /timestamp
```bash
curl -X POST -H "Content-Type: text/plain" --data "1700000000" http://localhost:8080/timestamp
```
GET /timestamp
```bash
curl http://localhost:8080/timestamp
```

Notes
The pod will restart because the app exits after printing the timestamp.
This behavior is intentional and matches the assignment requirements.
The goal is to demonstrate Docker + Kubernetes deployment, not a long‑running service.

