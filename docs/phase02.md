✅ Phase 2: Value-Added Features – Daily Plan (Weeks 7–12)
Duration: 6 weeks
Developer: Solo
Focus: Team collaboration, resource management, content editing, domain setup


👥 Week 7: Organization & Team Collaboration Service

| Day        | Tasks                                                                   | Est. Time |
| ---------- | ----------------------------------------------------------------------- | --------- |
| **Day 31** | Create `team` service (FastAPI), MongoDB schema for teams, roles        | 5h        |
| **Day 32** | Invite users to teams (email + token-based link), join/leave team logic | 6h        |
| **Day 33** | Add permission matrix (owner, editor, viewer), middleware               | 6h        |
| **Day 34** | Add endpoints for team settings, remove members, change roles           | 5h        |
| **Day 35** | Test IAM ↔ Team integration, document API usage                         | 5h        |

📁 Week 8: Resource Management Service

| Day        | Tasks                                                                 | Est. Time |
| ---------- | --------------------------------------------------------------------- | --------- |
| **Day 36** | Create `resource` service (FastAPI), schema for docs/images/code/etc. | 6h        |
| **Day 37** | Implement resource versioning, tagging, and sharing controls          | 5h        |
| **Day 38** | Add ACLs for public/private/tenant-scoped resources                   | 6h        |
| **Day 39** | Test file linking with `storage` service, add download tracking       | 5h        |
| **Day 40** | UI + API tests for resource CRUD with team scope                      | 5h        |

🧑‍🎨 Week 9: Studio Editor Service
| Day        | Tasks                                                                    | Est. Time |
| ---------- | ------------------------------------------------------------------------ | --------- |
| **Day 41** | Create `studio` service for creative editing (initial text/image editor) | 6h        |
| **Day 42** | Implement section/page-based structure, collaborative lock draft         | 6h        |
| **Day 43** | Auto-save drafts, support file embed from resource storage               | 5h        |
| **Day 44** | Integrate user cursor presence for collaboration (Redis/pubsub)          | 6h        |
| **Day 45** | Minimal frontend testing (if applicable), bug fixes                      | 5h        |


🌐 Week 10: Domain & Subdomain Management
| Day        | Tasks                                                                | Est. Time |
| ---------- | -------------------------------------------------------------------- | --------- |
| **Day 46** | Create `domain` service (FastAPI), domain/subdomain schema           | 6h        |
| **Day 47** | Implement domain verification (DNS TXT check), subdomain claim logic | 6h        |
| **Day 48** | Tenant resolution logic in API Gateway by domain/subdomain           | 6h        |
| **Day 49** | Store verified domains in MongoDB, update tenant config              | 5h        |
| **Day 50** | End-to-end test: domain claim → resolve → access Studio page         | 5h        |


⚙️ Week 11: Admin Panel + Feature Toggles
| Day        | Tasks                                                       | Est. Time |
| ---------- | ----------------------------------------------------------- | --------- |
| **Day 51** | Create internal admin dashboard (FastAPI + Jinja2 or React) | 5h        |
| **Day 52** | List/manage users, tenants, usage quotas, current plan      | 6h        |
| **Day 53** | Add feature flag toggles (MongoDB driven) by plan           | 5h        |
| **Day 54** | Enable/disable services/modules per tenant/subscription     | 6h        |
| **Day 55** | Admin audit logs and activity feeds                         | 5h        |


🧪 Week 12: QA, Integration, Deployment

| Day        | Tasks                                                              | Est. Time |
| ---------- | ------------------------------------------------------------------ | --------- |
| **Day 56** | Merge all microservices into staging env, manual walkthroughs      | 6h        |
| **Day 57** | Write integration tests across services (team ↔ studio ↔ resource) | 5h        |
| **Day 58** | Performance test: collaborative editing, domain resolution         | 5h        |
| **Day 59** | Fix bugs, add missing test cases, improve logging & alerts         | 6h        |
| **Day 60** | Tag Phase 2 release, update project board & docs                   | 4h        |

📊 Summary by Service (Phase 2)
| Component             | Est. Time |
| --------------------- | --------- |
| Team Collaboration    | 27h       |
| Resource Management   | 27h       |
| Studio Editor         | 28h       |
| Domain Management     | 28h       |
| Admin Panel + Toggles | 27h       |
| QA & Deployment       | 26h       |
| **Total**             | \~163h    |
