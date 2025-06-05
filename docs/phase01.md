✅ Phase 1: Foundation & Core Services – Daily Plan
Duration: 6 weeks
Working Style: Solo Developer, ~5–6 hrs/day
Goals: Project scaffolding, authentication, storage, billing, basic notifications



🔧 Week 1: Project Bootstrapping & Scaffolding

| Day       | Tasks                                                                                                  | Est. Time |
| --------- | ------------------------------------------------------------------------------------------------------ | --------- |
| **Day 1** | Set up monorepo (or polyrepo) structure, create `iam`, `gateway`, `common` service scaffolds (FastAPI) | 5h        |
| **Day 2** | Set up Docker, Docker Compose for local dev with hot reload, healthcheck endpoints                     | 6h        |
| **Day 3** | Configure MongoDB container with tenant-aware schema design; create dev DBs                            | 5h        |
| **Day 4** | Set up Azure DevOps pipelines (CI), linting, and FastAPI test boilerplate                              | 6h        |
| **Day 5** | API Gateway (Traefik/NGINX): route requests to IAM service with JWT passthrough                        | 6h        |


👤 Week 2: IAM Service – Authentication & Tenant Management

| Day        | Tasks                                                                    | Est. Time |
| ---------- | ------------------------------------------------------------------------ | --------- |
| **Day 6**  | Build user registration/login, JWT issuance/validation (FastAPI + PyJWT) | 5h        |
| **Day 7**  | Add role-based access control (RBAC) system, global vs tenant scopes     | 6h        |
| **Day 8**  | Tenant registration + org model; associate users to tenants              | 6h        |
| **Day 9**  | Add `@requires_permission()` decorators, write unit tests for auth logic | 5h        |
| **Day 10** | Integrate IAM into API Gateway for request validation                    | 6h        |

💾 Week 3: Storage Service – File Uploads

| Day        | Tasks                                                               | Est. Time |
| ---------- | ------------------------------------------------------------------- | --------- |
| **Day 11** | Create `storage` service (FastAPI), integrate MongoDB for metadata  | 5h        |
| **Day 12** | Integrate AWS S3-compatible storage (e.g., MinIO for local dev)     | 6h        |
| **Day 13** | Implement presigned upload/download URLs, file validation           | 5h        |
| **Day 14** | Add image resizing/optimization (e.g., Pillow, file-type detection) | 6h        |
| **Day 15** | Write tests, setup file upload UI (minimal) to verify end-to-end    | 5h        |

💳 Week 4: Subscription & Billing Service – Stripe Integration

| Day        | Tasks                                                                                  | Est. Time |
| ---------- | -------------------------------------------------------------------------------------- | --------- |
| **Day 16** | Create `billing` service (FastAPI), pricing plan model in MongoDB                      | 5h        |
| **Day 17** | Setup Stripe dev account, create test products/plans                                   | 4h        |
| **Day 18** | Integrate Stripe checkout/session + webhook endpoints (SubscriptionCreated, Cancelled) | 6h        |
| **Day 19** | Connect with IAM service (enable/disable features per plan)                            | 5h        |
| **Day 20** | Add invoice history + test failure recovery logic                                      | 5h        |

📣 Week 5: Notification Service – Email, Events

| Day        | Tasks                                                               | Est. Time |
| ---------- | ------------------------------------------------------------------- | --------- |
| **Day 21** | Create `notification` service (FastAPI), MongoDB for templates/logs | 5h        |
| **Day 22** | Integrate SendGrid for email sending + retry queue                  | 6h        |
| **Day 23** | Setup Redis pub/sub or simple event queue for async triggers        | 6h        |
| **Day 24** | Define event contract for `UserRegistered`, `SubscriptionCreated`   | 5h        |
| **Day 25** | End-to-end testing from IAM → Event → Notification Email            | 5h        |

🧪 Week 6: Integration, Tests, Staging Setup

| Day        | Tasks                                                              | Est. Time |
| ---------- | ------------------------------------------------------------------ | --------- |
| **Day 26** | Add service discovery (Docker DNS), document all routes in OpenAPI | 5h        |
| **Day 27** | Write integration tests (IAM ↔ Storage ↔ Billing ↔ Notification)   | 6h        |
| **Day 28** | Setup staging env in Azure, deploy all services (via Azure DevOps) | 6h        |
| **Day 29** | Manual end-to-end UAT walkthrough, fix bugs                        | 5h        |
| **Day 30** | Freeze Phase 1 snapshot, create release notes                      | 4h        |


📌 Summary: Time Allocation by Service
| Component        | Est. Total Time           |
| ---------------- | ------------------------- |
| IAM Service      | 25h                       |
| Storage Service  | 27h                       |
| Billing Service  | 25h                       |
| Notification     | 27h                       |
| DevOps + Gateway | 25h                       |
| Integration/Test | 26h                       |
| **Total**        | \~155–160 hours (6 weeks) |
