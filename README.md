🚀 K8s Observability & GitOps Lab
Engineer: Haifa Alanesi

Live Dashboard: https://monitoring.haifa.work

📋 Project Overview
This project demonstrates a production-grade monitoring stack deployed on a local Ubuntu Kubernetes cluster. By leveraging GitOps principles, the entire infrastructure is managed as code, ensuring self-healing capabilities and secure remote access without exposing local ports to the internet.


<img width="1024" height="471" alt="image" src="https://github.com/user-attachments/assets/a0b540a1-84f7-4ad2-ac79-7e4888f130cc" />










🛠️ The Tech Stack
Orchestration: Kubernetes (K3s)

GitOps: FluxCD

Database: MySQL 8.0 (Persistent Storage)

Visualization: Grafana

Security: Cloudflare Zero Trust (Tunnels)

🏗️ System Architecture
The following diagram illustrates the secure data flow from my local hardware to the public web dashboard.

💡 Key Features & Challenges Solved
1. Zero-Trust Connectivity
Instead of traditional port forwarding, I implemented Cloudflare Tunnels. This creates an outbound-only connection from the cluster to the Cloudflare Edge, keeping my home network hidden while providing a professional domain (monitoring.haifa.work).

2. Infrastructure as Code (GitOps)
Using FluxCD, any change pushed to this repository is automatically reconciled in the cluster. This eliminated "configuration drift" and allowed me to manage secrets and deployments version-by-version.

3. Persistent Data Monitoring
Configured MySQL with specific fsGroup security contexts to handle Linux volume permissions, ensuring that my power usage metrics are saved even if the pods restart.

📊 Dashboard Preview
My Grafana dashboard visualizes real-time power consumption across my lab devices (Server-01, Switch-01, Access-Point). I utilized SQL aggregations and dynamic thresholds to provide immediate visual status alerts.


<img width="1901" height="1025" alt="image" src="https://github.com/user-attachments/assets/5e0028f1-b185-4338-8e99-55d6439a78ea" />



🚀 How to Run
Ensure flux is installed on your cluster.

Clone this repository.

Apply the bootstrap configuration:

Bash
flux reconcile kustomization flux-system --with-source
