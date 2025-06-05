# Portfolio MVP Plan with DevOps / CI/CD First Approach
Total Duration: 12 weeks (Weeks 1–12)
Stack: FastAPI, MongoDB, Node.js, Azure DevOps


Phase 1: Foundation & Core Services + DevOps Setup (Weeks 1–6)

| Week   | Goals & Tasks                                                                                                                                                                                                                                                                                            | Estimated Effort |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Week 1 | **DevOps Pipeline Setup:**<br>- Create Azure DevOps project and repo<br>- Setup branching strategy (Gitflow or trunk-based)<br>- Configure build pipeline for FastAPI and Node.js microservices<br>- Configure Docker builds and container registry<br>- Setup linting, code formatting checks in CI     | 20h              |
| Week 2 | **CI/CD Enhancements:**<br>- Add automated unit tests run on pipeline<br>- Setup MongoDB test environment (local or Azure Cosmos DB emulator)<br>- Implement security scanning in CI (e.g., dependency vulnerability checks)<br>- Configure environment variables and secrets management in Azure DevOps | 20h              |
| Week 3 | **Core Microservices Development Begin:**<br>- IAM Service skeleton (FastAPI)<br>- Storage Service skeleton (FastAPI)<br>- Initial API Gateway setup (reverse proxy or Azure API Management)<br>- Deploy microservices to Azure Kubernetes Service (AKS) dev cluster                                     | 25h              |

| Day       | Hours | Tasks                                                                                                                                                                                             |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** | 5h    | 🔹 Scaffold IAM Service (FastAPI) using `uv`\n🔹 Set up base project structure (routers, schemas, services, config, envs)\n🔹 Set up logging, health check route                                  |
| **Day 2** | 5h    | 🔹 Scaffold Storage Service (FastAPI) with similar structure\n🔹 Add `/upload`, `/download`, and `/presign` placeholders\n🔹 Add dummy S3-compatible integration (e.g., MinIO locally)            |
| **Day 3** | 5h    | 🔹 Set up local `docker-compose` for IAM, Storage, and MongoDB\n🔹 Add initial `Dockerfile` for each service\n🔹 Write Helm charts or K8s manifests for IAM and Storage                           |
| **Day 4** | 5h    | 🔹 Set up AKS dev cluster (if not already)\n🔹 Push Docker images to Azure Container Registry (ACR)\n🔹 Deploy IAM and Storage service to AKS\n🔹 Configure Azure API Management or NGINX Ingress |
| **Day 5** | 5h    | 🔹 Test access via API Gateway (manual curl or Swagger UI)\n🔹 Set up GitHub Actions/Azure Pipelines for CI\n🔹 Deploy on commit (basic pipeline setup for both services)                         |



| Week 4 | **IAM Service Development:**<br>- User registration, login, JWT issuance<br>- Role and tenant management<br>- Integration with API Gateway for authentication<br>- CI pipeline testing and deployment automation improvements                                                                            | 25h              |
| Week 5 | **Storage Service Development:**<br>- File upload/download APIs<br>- Integration with Azure Blob Storage (S3-compatible)<br>- Pre-signed URL generation<br>- CI/CD deployment validation<br>- Setup monitoring and logging for these services                                                            | 25h              |
| Week 6 | **Notification Service Setup (Optional MVP support):**<br>- Basic email notifications (SendGrid)<br>- Queue setup with Redis/Azure Cache for messages<br>- Deploy and monitor<br>- Finalize and test CI/CD pipeline workflows                                                                            | 20h              |


| Day       | Hours | Tasks                                                                                                                                                      |
| --------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** | 5h    | 🔹 Implement user registration & login (JWT)\n🔹 Use secure password hashing (`passlib`, `bcrypt`)\n🔹 Define Pydantic models & basic validation           |
| **Day 2** | 5h    | 🔹 Implement JWT token handling (access/refresh)\n🔹 Add middleware to validate JWT\n🔹 Secure routes via dependency injection                             |
| **Day 3** | 5h    | 🔹 Build tenant model: Create tenant, assign users\n🔹 Build role model: Define roles, attach to users per tenant\n🔹 CRUD APIs for roles and tenants      |
| **Day 4** | 5h    | 🔹 Connect IAM to API Gateway (Azure APIM or NGINX)\n🔹 Ensure JWT is verified by IAM for incoming requests\n🔹 Add `whoami` route to test auth context    |
| **Day 5** | 5h    | 🔹 Write unit tests (pytest)\n🔹 Improve CI: Lint (ruff), test, Docker build & push\n🔹 Auto-deploy IAM on push to `main` (Azure Pipelines/GitHub Actions) |


Phase 2: Portfolio Service + DevOps Refinement (Weeks 7–12)

| Week    | Goals & Tasks                                                                                                                                                                                                            | Estimated Effort |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| Week 7  | **Portfolio Service Development:**<br>- Define MongoDB schema for portfolios, assets, branding<br>- CRUD API for portfolio management<br>- Connect with Storage Service for asset linking<br>- Local integration testing | 25h              |
| Week 8  | **Portfolio Service Continued:**<br>- Implement template selection and branding settings<br>- Add validations and error handling<br>- Unit & integration tests<br>- Add to CI/CD pipelines                               | 25h              |
| Week 9  | **Deploy Portfolio Service:**<br>- Deploy to AKS<br>- Configure ingress/API Gateway routes<br>- Setup metrics and logs (Azure Monitor/Prometheus/Grafana)<br>- Performance baseline testing                              | 20h              |
| Week 10 | **End-to-End Integration:**<br>- Test interactions between IAM, Storage, and Portfolio Services<br>- End-to-end API Gateway request flow<br>- Add automated integration tests to pipeline                                | 20h              |
| Week 11 | **DevOps Pipeline Enhancements:**<br>- Implement blue-green or canary deployments in AKS<br>- Setup alerting for service failures/deployments (Azure Alerts)<br>- Document deployment and rollback procedures            | 20h              |
| Week 12 | **Final QA and MVP Polish:**<br>- Fix bugs identified in tests<br>- Run load tests<br>- Finalize API documentation (OpenAPI/Swagger)<br>- Prepare MVP demo and release notes                                             | 20h              |


| Aspect          | Description                                     |
| --------------- | ----------------------------------------------- |
| **Focus**       | DevOps-first to enable reliable, fast delivery  |
| **CI/CD Tools** | Azure DevOps Pipelines, AKS, Azure Blob Storage |
| **Testing**     | Automated unit, integration, and load tests     |
| **Monitoring**  | Logging and metrics setup from early stages     |
| **Deployment**  | Containerized microservices with Kubernetes     |
