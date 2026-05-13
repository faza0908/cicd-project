# CI/CD Pipeline Final Project

## Project Name: Automated CI/CD Pipeline with GitHub Actions and OpenShift Tekton

### Project Overview

This project demonstrates the implementation of a complete CI/CD (Continuous Integration/Continuous Deployment) pipeline using:

- **GitHub Actions** for automated linting and unit testing
- **OpenShift Tekton Pipelines** for full deployment automation
- **Python Flask** as the application framework
- **Flake8** for Python linting
- **Nose** for unit testing
- **Buildah** for container image building
- **OpenShift** for container orchestration and deployment

---

## Project Structure

```
cicd-project/
├── .github/
│   └── workflows/
│       └── workflow.yml          # GitHub Actions CI workflow
├── .tekton/
│   └── tasks.yml                 # Tekton pipeline tasks
├── tests/
│   └── test_app.py               # Unit tests
├── app.py                        # Main Flask application
├── requirements.txt              # Python dependencies
├── setup.cfg                     # Configuration for flake8 and nose
├── Dockerfile                    # Container build instructions
└── README.md                     # Project documentation
```

---

## Application

A RESTful Python Flask application that provides a simple counter service running on **port 8000**.

### Features
- Health check endpoint (`/health`)
- Counter service with CRUD operations
- JSON API responses

---

## CI/CD Pipeline Steps

### GitHub Actions Workflow
1. **Checkout** – Pulls the latest code from the repository
2. **Set up Python** – Configures Python 3.9 environment
3. **Install dependencies** – Installs all required packages
4. **Lint with Flake8** – Checks code quality and style
5. **Run unit tests with Nose** – Executes all unit tests

### OpenShift Tekton Pipeline
1. **cleanup** – Removes old workspace contents
2. **git-clone** – Clones the GitHub repository
3. **flake8** – Lints the Python code
4. **nose** – Runs the unit test suite
5. **buildah** – Builds and pushes the container image
6. **deploy** – Deploys the application to OpenShift

---

## Getting Started

### Prerequisites
- Python 3.9+
- OpenShift CLI (`oc`)
- Tekton CLI (`tkn`)

### Local Development

```bash
# Clone the repository
git clone https://github.com/<your-username>/cicd-project.git
cd cicd-project

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Run tests
nosetests
```

### Running Lint

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
```

---

## Author

**Student Name** – IBM DevOps and Software Engineering Professional Certificate  
**Course**: CI/CD Final Project  
**Date**: 2024

---

## License

This project is licensed under the Apache License 2.0 – see the LICENSE file for details.
