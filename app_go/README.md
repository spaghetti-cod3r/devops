# App Title

**Moscow Time Web Application**

[![CI-GO](https://github.com/spaghetti-cod3r/devops/actions/workflows/ci_go.yml/badge.svg)](https://github.com/spaghetti-cod3r/devops/actions/workflows/ci_go.yml)

# Description

This is a simple Go web application that fetches the current time in Moscow using TimeAPI and displays it in a visually appealing HTML interface.

# Features

- Fetches the current time in Moscow via an external API.
- Displays the time in a clean and responsive web interface.
- Handles errors gracefully and provides fallback behavior in case of issues.

# Installation:

## 1. Normal Installation:

### Requirements

- Linux OS
- Go >= 1.23
- Web browser

1. Clone the repository
2. Run the application:

   ```bash
   go run app.go
   ```
3. Open your browser and navigate to:

   ```
   http://127.0.0.1:8000
   ```
4. To exit the app, press ``(Ctrl + C)``

## 2. Installation Using a Docker Image

### Requirements

- Docker
- Web browser

1. Pull the dockerized image from docker hub

   ```bash
   docker pull spaghettic0der/moscow-time-go:latest
   ```
2. Run the image on any free port (e.g. 8000)

   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/moscow-time-go:latest
   ```
3. Open your browser and navigate to:

   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```
4. To stop the app, press ``Ctrl + C``

## 3. Installation Using a Distroless Docker Image

### Requirements

- Docker
- Web browser

1. Pull the dockerized image from docker hub

   ```bash
   docker pull spaghettic0der/distro-moscow-time:v2.0.0
   ```
2. Run the image on any free port (e.g. 8000)

   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/distro-moscow-time:v2.0.0
   ```
3. Open your browser and navigate to:

   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```
4. To stop the app, press ``Ctrl + C``

---

## 4. Using Docker Compose

### Requirements

- Docker and Docker Compose
- Web browser

1. Create `docker-compose.yml` file with the following content:

   ```
   version: '3.8'

   services:
     app:
       image: docker pull spaghettic0der/moscow-time-go:v2.0.0

       ports:
         - "8000:8000"
       volumes:
         - ./data:/data
   ```
2. Specify the port in the docker-compose file (e.g. 8000):

   ```
   ports:
         - "8000:8000"
   ```
3. Run the docker-compose file using:

   ```bash
   docker-compose up -d
   ```
4. Open your browser and navigate to:

   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```
5. To display the visit counts, navigate to:

   ```bash
   http://127.0.0.1:<Your-Selected-Port>/visits
   ```
6. To stop the app, press ``Ctrl + C``

**Note**: the visit count will be saved locally inside `data/visits.txt`

# Workflow Overview

The CI workflow for the `moscow-time-go` project performs the following steps:

1. **Checkout Code**: The latest code is checked out from the repository using the `actions/checkout` action.
2. **Run Snyk Security Scan**: The workflow uses the `snyk/actions/golang` action to run a security scan on the Go code to check for vulnerabilities. It requires the `SNYK_TOKEN` secret for authentication.
3. **Log in to Docker Hub**: The workflow logs into Docker Hub using the `docker/login-action@v3` action with credentials stored in GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).
4. **Build Docker Image**: The workflow navigates to the `app_go` directory and builds a Docker image with the `latest` tag, which contains the Go application.
5. **Push Docker Image**: The Docker image built in the previous step is pushed to Docker Hub for deployment or further use.

## Triggering the Workflow

This workflow is triggered on the following events:

- **Push**: When code is pushed to `lab3` branch, and changes are made to files in the `app_go` directory.
- **Pull Request**: When a pull request is opened or updated on the `lab3` branch, and changes are made to files in the `app_go` directory.

## Secrets Required

To successfully run this workflow, the following secrets must be added to the GitHub repository:

- `SNYK_TOKEN`: Your Snyk authentication token.
- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password or an access token.

## Example of Workflow Trigger

The workflow can be triggered by creating or updating a pull request, like this:

```bash
git checkout lab3
git push origin lab3
```
