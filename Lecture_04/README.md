# Docker Network - Fundamental Commands

## Network Management Commands

### List Networks
```bash
# List all Docker networks
docker network ls

# List networks with detailed information
docker network ls --format "table {{.ID}}\t{{.Name}}\t{{.Driver}}\t{{.Scope}}"
```

### Create Networks
```bash
# Create a bridge network (default)
docker network create my-network

# Create a network with specific driver
docker network create --driver bridge my-bridge-network

# Create a network with custom subnet
docker network create --subnet=172.20.0.0/16 my-custom-network

# Create a network with IP range
docker network create --subnet=172.20.0.0/16 --ip-range=172.20.240.0/20 my-range-network
```

### Inspect Networks
```bash
# Inspect a specific network
docker network inspect bridge

# Inspect multiple networks
docker network inspect my-network another-network

# Get specific information using format
docker network inspect --format='{{.IPAM.Config}}' my-network
```

### Remove Networks
```bash
# Remove a specific network
docker network rm my-network

# Remove multiple networks
docker network rm network1 network2

# Remove all unused networks
docker network prune

# Remove all unused networks without confirmation
docker network prune -f
```

## Container Network Operations

### Connect Containers to Networks
```bash
# Run container with default network
docker run -d --name my-container nginx

# Run container with specific network
docker run -d --name my-container --network my-network nginx

# Run container with custom IP
docker run -d --name my-container --network my-network --ip 172.20.0.10 nginx

# Connect running container to network
docker network connect my-network my-container

# Connect with alias
docker network connect --alias web-server my-network my-container
```

### Disconnect Containers from Networks
```bash
# Disconnect container from network
docker network disconnect my-network my-container

# Force disconnect
docker network disconnect -f my-network my-container
```

## Network Isolation and Communication

### Disable Networking
```bash
# Run container with no networking
docker run -it --rm --network none busybox:latest

# Run container with host networking
docker run -it --rm --network host busybox:latest
```

### Port Publishing
```bash
# Publish specific port
docker run -d -p 8080:80 --name web-server nginx

# Publish to specific interface
docker run -d -p 127.0.0.1:8080:80 --name web-server nginx

# Publish all exposed ports
docker run -d -P --name web-server nginx

# Publish UDP port
docker run -d -p 53:53/udp --name dns-server my-dns-image
```

## Network Drivers

### Bridge Network (Default)
```bash
# Create bridge network
docker network create --driver bridge my-bridge

# Create bridge with custom options
docker network create \
  --driver bridge \
  --subnet=172.30.0.0/16 \
  --gateway=172.30.0.1 \
  my-custom-bridge
```

### Host Network
```bash
# Use host networking
docker run --network host my-app
```

### Overlay Network (Swarm)
```bash
# Create overlay network (requires swarm mode)
docker network create --driver overlay my-overlay

# Create encrypted overlay network
docker network create --driver overlay --opt encrypted my-secure-overlay
```

### Macvlan Network
```bash
# Create macvlan network
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  my-macvlan
```

## Advanced Network Commands

### Network Troubleshooting
```bash
# Check network connectivity between containers
docker exec -it container1 ping container2

# Check network configuration
docker exec -it my-container ip addr show

# Check routing table
docker exec -it my-container ip route

# Check DNS resolution
docker exec -it my-container nslookup container2

# Check listening ports
docker exec -it my-container netstat -tlnp
```

### Network Filters
```bash
# List networks by driver
docker network ls --filter driver=bridge

# List networks by name pattern
docker network ls --filter name=my-*

# List dangling networks
docker network ls --filter dangling=true
```

## Docker Compose Network Commands

### Basic Network Definition
```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    image: nginx
    networks:
      - frontend
  
  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
```

### Compose Network Operations
```bash
# Create networks defined in compose file
docker-compose up -d

# View compose networks
docker-compose ps

# Remove compose networks
docker-compose down

# Remove networks and volumes
docker-compose down -v
```

## Best Practices

1. **Use Custom Networks**: Avoid using the default bridge network for multi-container applications
2. **Network Segmentation**: Create separate networks for different application tiers
3. **Use Aliases**: Assign meaningful aliases to containers for service discovery
4. **Clean Up**: Regularly remove unused networks with `docker network prune`
5. **Security**: Use internal networks for backend services that don't need external access

## Common Network Types Summary

| Network Type | Use Case | Isolation | Performance |
|--------------|----------|-----------|-------------|
| Bridge | Single host, multi-container apps | Container-level | Good |
| Host | High performance, single container | None | Excellent |
| Overlay | Multi-host, swarm services | Service-level | Good |
| Macvlan | Legacy apps, direct network access | VLAN-level | Excellent |
| None | Maximum security, no networking | Complete | N/A |

## Examples

### Multi-tier Application
```bash
# Create networks
docker network create frontend-net
docker network create backend-net

# Run database (backend only)
docker run -d --name db --network backend-net postgres

# Run API server (both networks)
docker run -d --name api --network backend-net nginx
docker network connect frontend-net api

# Run web server (frontend only)
docker run -d --name web --network frontend-net -p 80:80 nginx
```

### Network with Custom DNS
```bash
# Create network with custom DNS
docker network create --dns=8.8.8.8 --dns=8.8.4.4 my-dns-network

# Run container with custom hostname
docker run -d --name web --hostname web-server --network my-dns-network nginx
```
