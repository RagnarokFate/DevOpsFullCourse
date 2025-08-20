# Lecture 03 Summary: Docker Images, Containers, and Volumes

## Overview
This lecture covers the creation and management of Docker images and containers for two applications:
- **Flask App** (`flask-app`)
- **Spring Music App** (`jb_dockerfile`)

It also introduces Docker volumes, their types, and common commands for volume management.

---

## Docker Image & Container Creation

### 1. Flask App (`flask-app`)
**Dockerfile Summary:**
- Uses `python:3.11.9` as the base image
- Sets the working directory to `/usr/src/app`
- Copies all files into the container
- Installs dependencies from `requirements.txt`
- Exposes port `5000`
- Runs the app with `python app.py`

**Build & Run Commands:**
```sh
# Build the image
docker build -t flask-app-image .

# Run the container
docker run --rm -p 5000:5000 flask-app-image
```

### 2. Spring Music App (`jb_dockerfile`)
**Dockerfile Summary:**
- Uses `yanivomc/alpine-oraclejdk8:slim` as the base image
- Sets the working directory to `/app`
- Copies `artifacts/spring-music.jar` into the container
- Exposes port `8080`
- Runs the JAR file with Java

**Build & Run Commands:**
```sh
# Build the image
docker build -t spring-music-image .

# Run the container
docker run --rm -p 8080:8080 spring-music-image
```

---

## Docker Volumes
Docker volumes are used to persist and share data between containers and the host system. They are the preferred way to store data in Docker.

### Types of Docker Volumes
1. **Named Volumes**
   - Managed by Docker
   - Created with a specific name
   - Example: `mydata`
2. **Anonymous Volumes**
   - No explicit name
   - Created automatically by Docker
3. **Host Bind Mounts**
   - Maps a directory or file from the host to the container
   - Example: `/host/path:/container/path`

### Common Volume Commands & Objectives
| Command | Objective |
|---------|-----------|
| `docker volume create mydata` | Create a named volume |
| `docker volume ls` | List all volumes |
| `docker volume inspect mydata` | View details about a volume |
| `docker volume rm mydata` | Remove a volume |
| `docker run -v mydata:/data ...` | Attach a named volume to a container |
| `docker run -v /host/path:/container/path ...` | Use a bind mount |

---

## File Structure
```
lecture_03/
├── flask-app/
│   ├── app.py
│   ├── requirements.txt
│   ├── dockerfile
│   └── templates/
├── jb_dockerfile/
│   ├── Dockerfile
│   └── artifacts/
│       └── spring-music.jar
└── README.md   # <--- This summary file
```

---

## Conclusion
This lecture provided practical experience in building and running Docker containers for Python and Java applications, and introduced persistent storage using Docker volumes. Mastery of these concepts is essential for modern DevOps workflows.
