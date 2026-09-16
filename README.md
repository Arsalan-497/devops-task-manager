# DevOps Task Manager

A containerized Django task management application built to demonstrate practical DevOps concepts including Docker, PostgreSQL, CI/CD, automated testing, Docker image delivery, health checks, and deployment workflows.

## Architecture

```text
Developer
    │
    ▼
 GitHub Repository
    │
    ▼
GitHub Actions
    ├── Django checks
    ├── Automated tests
    ├── Docker image build
    └── Docker Hub push
            │
            ▼
       Docker Hub
            │
            ▼
   Local Deployment
            │
       ┌────┴────┐
       ▼         ▼
    Django   PostgreSQL
    +Gunicorn
```

## Features

* Create and manage tasks
* Mark tasks as completed or incomplete
* Delete tasks
* PostgreSQL database
* Dockerized application
* Docker Compose configuration
* Environment-based configuration
* Gunicorn application server
* Automatic database migrations on container startup
* Application health endpoint
* Docker container health checks
* Automated Django tests
* GitHub Actions CI/CD pipeline
* Docker image publishing to Docker Hub
* Commit SHA image tagging
* Deployment configuration included in the repository

## Technologies

* Python
* Django
* PostgreSQL
* Docker
* Docker Compose
* Gunicorn
* Git & GitHub
* GitHub Actions
* Docker Hub
* Linux / Ubuntu

## Project Structure

```text
devops-task-manager/
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
├── tasks/
├── deployment/
│   ├── docker-compose.yml
│   └── .env.example
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── manage.py
└── README.md
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Arsalan-497/devops-task-manager.git
cd devops-task-manager
```

### 2. Configure environment variables

Create a `.env` file in the project root with the following variables:

```text
POSTGRES_DB=taskmanager
POSTGRES_USER=taskmanager
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Start the application

```bash
docker compose up -d --build
```

The application will be available at:

```text
http://localhost:8000
```

### 4. Check container health

```bash
docker compose ps
```

The application and database containers should report a healthy status.

### 5. Stop the application

```bash
docker compose down
```

The PostgreSQL data volume is preserved unless it is explicitly removed.

## Health Check

The application provides a health endpoint:

```text
/health/
```

Example:

```bash
curl http://localhost:8000/health/
```

Expected response:

```json
{"status": "ok"}
```

Docker also monitors the application through its configured health check.

## Testing

The project includes automated Django tests.

Run:

```bash
docker compose exec web python manage.py test
```

The CI pipeline also runs the tests automatically on pushes and pull requests to the `main` branch.

## CI/CD Pipeline

GitHub Actions performs the following steps:

1. Checks out the repository
2. Sets up Python 3.12
3. Starts PostgreSQL for testing
4. Installs Python dependencies
5. Runs Django system checks
6. Runs automated tests
7. Builds the Docker image
8. Tags the image with `latest`
9. Tags the image with the Git commit SHA
10. Pushes the images to Docker Hub

## Docker Image

The application image is published to:

```text
arsalkhan497/devops-task-manager
```

Versioned images use the Git commit SHA so specific builds can be identified and deployed.

## Deployment

The repository contains a separate deployment configuration:

```text
deployment/docker-compose.yml
```

It pulls the application image from Docker Hub instead of building the application locally.

The deployment configuration includes:

* Django application container
* PostgreSQL container
* Persistent PostgreSQL volume
* Container restart policies
* Database health check
* Application health check
* Environment-based configuration

### Deployment configuration example

Create the deployment environment file:

```bash
cp deployment/.env.example deployment/.env
```

Update the values in `deployment/.env`, then run:

```bash
docker compose \
  --env-file deployment/.env \
  -f deployment/docker-compose.yml \
  pull
```

Start the deployment:

```bash
docker compose \
  --env-file deployment/.env \
  -f deployment/docker-compose.yml \
  up -d
```

Check the deployment:

```bash
docker compose \
  --env-file deployment/.env \
  -f deployment/docker-compose.yml \
  ps
```

## Deployment Note

This project has been validated using a local Ubuntu environment to simulate a deployment server. No public production server is claimed as part of this project.

The deployment configuration is designed so the same containerized workflow can be adapted to a remote server or cloud environment.

## DevOps Concepts Demonstrated

This project demonstrates practical experience with:

* Linux
* Git version control
* GitHub
* CI/CD
* Docker
* Docker Compose
* Container health monitoring
* PostgreSQL
* Environment variables
* Automated testing
* Docker image versioning
* Docker Hub
* Application deployment
* Infrastructure configuration

## Future Improvements

Possible future improvements include:

* Remote VPS deployment
* HTTPS with a reverse proxy
* Domain configuration
* Automated remote deployment
* Infrastructure as Code
* Monitoring and logging
* Container security improvements
* Cloud deployment
< CI/CD pipeline verified -->
