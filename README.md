# Aerochaser
Prereqs:
Download Minikube 
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube

start venv

To run locally with Flask:
flask run
Go to http link to test app

To run virtually on Docker: (do when file change)
docker build -t aero-app .
docker run -p 8080:80 aero-app

Now, in a separate terminal
start venv
minikube start

Deploying to Kubernetes: (do when file change)
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Checking status
minikube status
  Expect to see:
  minikube
  type: Control Plane
  host: Running
  kubelet: Running
  apiserver: Running
  kubeconfig: Configured

kubectl get svc aero-app-service

Useful things:
  kubectl get pods
  kubectl logs <pod_id>


When using AWS EC2 with ELB (elastic load balancer), replace service.yaml with

apiVersion: v1
kind: Service
metadata:
  name: aero-app-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-internal: "false" # Set to "true" if using an internal ELB
spec:
  selector:
    app: aero-app
  ports:
    - protocol: "TCP"
      port: 80
      targetPort: 80
  type: LoadBalancer
