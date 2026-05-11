# 🛡️ DevSecOps Pipeline (Python)
[![DevSecOps Optimized Pipeline](https://github.com/Muskan-kumari17/devsecops-project/actions/workflows/devsecops.yml/badge.svg)](https://github.com/Muskan-kumari17/devsecops-project/actions/workflows/devsecops.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Security](https://img.shields.io/badge/Security-Hardened-success)

### Implementing a Secure CI/CD Pipeline with SAST & DAST using GitHub Actions

## 📖 Project Overview
This project demonstrates the implementation of **Shift-Left Security** by integrating automated security scanning into the software development lifecycle. It features a Python Flask application that is automatically analyzed, audited, and hardened through a custom GitHub Actions pipeline.

The goal is to ensure that no code reaches deployment without passing rigorous security checks at the code, dependency, and container levels.

---

## 🚀 Security Architecture (The Pipeline)
The pipeline is triggered on every `push` or `pull_request` and executes the following security layers:

### 1. SAST (Static Application Security Testing)
- **Tool:** `Bandit`
- **Action:** Scans source code for vulnerabilities like hardcoded secrets, insecure function calls, and improper host bindings.

### 2. SCA (Software Composition Analysis)
- **Tool:** `Safety`
- **Action:** Audits `requirements.txt` to identify libraries with known CVEs (Common Vulnerabilities and Exposures).

### 3. Container Security
- **Tool:** `Trivy`
- **Action:** Performs a filesystem scan of the Docker environment to detect OS-level vulnerabilities.

### 4. DAST (Dynamic Application Security Testing)
- **Tool:** `OWASP ZAP (Placeholder)`
- **Action:** Simulates runtime analysis to ensure the application is secure while actively running.

---

## 🏗️ Hardening Measures Taken
To achieve a "Zero-Vulnerability" security posture, I implemented the following:
* **Non-Root User:** Configured Docker to run as `appuser` to prevent privilege escalation.
* **Multi-Stage Build:** Used a "builder" stage to keep the final production image small and secure.
* **Secure Config:** Disabled Flask `debug` mode and transitioned to environment-based configurations.
* **Base Image:** Switched to `python:3.10-slim` to reduce the attack surface.

---

## 🛠️ Tech Stack
- **Framework:** Flask (Python)
- **CI/CD:** GitHub Actions
- **Containerization:** Docker
- **Security Suite:** Bandit, Safety, Trivy, ZAP

---

## 📊 Viewing Security Reports
Every successful pipeline run generates a downloadable audit trail:
1. Go to the **Actions** tab.
2. Select the latest **Green** run.
3. Scroll to **Artifacts** and download `security-reports`.

## 💻 Local Setup
```bash
# Clone the repository
git clone [https://github.com/Muskan-kumari17/devsecops-project.git](https://github.com/Muskan-kumari17/devsecops-project.git)

# Build the hardened image
docker build -t secure-flask-app .

# Run the container
docker run -p 5000:5000 secure-flask-app
