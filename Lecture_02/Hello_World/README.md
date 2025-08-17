# Hello World with Docker

This README provides a short introduction to Docker and demonstrates basic commands using the `hello-world` image. These commands help you verify your Docker installation and explore container management.

## Prerequisites

- Docker Desktop installed on your system.

## Basic Docker Commands

### 1. Pull the Hello World Image

```sh
docker pull hello-world
```
Downloads the `hello-world` image from Docker Hub.

### 2. List Docker Images

```sh
docker images
```
Displays all images available locally.

### 3. Run the Hello World Container

```sh
docker run hello-world
```
Runs a container using the `hello-world` image to test your Docker setup.
---

## Docker Commands Reference

Below is a summary of useful Docker commands grouped by category:

### General Info
- `docker help` — Show help for Docker commands
- `docker help run` — Show help for the `run` command
- `docker info` — Display system-wide information
- `docker version` — Show Docker version info
- `docker network ls` — List Docker networks

### Images
- `docker images` — List images
- `docker pull [IMAGE]` — Pull image from registry
- `docker push [IMAGE]` — Push image to registry

### Containers
- `docker run [OPTIONS] IMAGE` — Run a container
- `docker ps` — List running containers
- `docker ps -a` — List all containers
- `docker ps -l` — Show last created container
- `docker stop [CONTAINER]` — Stop a container
- `docker start [CONTAINER]` — Start a container
- `docker restart [CONTAINER]` — Restart a container
- `docker stats [CONTAINER]` — Show container stats
- `docker top [CONTAINER]` — Display running processes in a container
- `docker port [CONTAINER]` — List port mappings
- `docker inspect [CONTAINER]` — Detailed container info
- `docker inspect -f "{{ .State.StartedAt }}" [CONTAINER]` — Show container start time
- `docker rm [CONTAINER]` — Remove a container

---

## Example: Run a Custom Docker Container

You can run a Docker container using the following command:

```sh
docker run -i -t -d --name dockerlearning -p 8080:80 alpine:latest
```
- `-i` — Interactive mode
- `-t` — Allocate a pseudo-TTY
- `-d` — Detached mode (run in background)
- `--name dockerlearning` — Name the container
- `-p 8080:80` — Map port 8080 on host to port 80 in container
- `alpine:latest` — Use the Alpine Linux image

You can add more options, commands, and arguments as needed to customize the container's behavior.
