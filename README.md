# Scalable E-Commerce Platform

This repository provides a microservices-based starter for a scalable e-commerce platform. Each core capability is implemented as an independently deployable FastAPI service and orchestrated with Docker Compose.

## Services

| Service | Responsibility | Port |
| --- | --- | --- |
| API Gateway | Entry point for client traffic | 8000 |
| User Service | User registration, authentication, profiles | 8001 |
| Product Catalog Service | Product listings, categories, inventory | 8002 |
| Shopping Cart Service | Cart management | 8003 |
| Order Service | Order placement and status | 8004 |
| Payment Service | Payment processing | 8005 |
| Notification Service | Email/SMS notifications | 8006 |

## Getting Started

1. Build and run the services:

```bash
docker compose up --build
```

2. Verify the services:

```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

## Next Steps

- Replace sample handlers with real business logic and data stores.
- Add inter-service communication (REST or gRPC).
- Introduce service discovery, centralized logging, and monitoring.
- Integrate CI/CD pipelines for automated testing and deployment.
