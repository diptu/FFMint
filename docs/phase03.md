✅ Phase 3: Subscription & Monetization – Daily Plan (Weeks 13–18)
Duration: 6 weeks
Focus: Stripe integration, pricing plans, tenant-level billing, feature locking, usage tracking, and user dashboard.


💳 Week 13: Subscription Plan Service
| Day        | Tasks                                                                         | Est. Time |
| ---------- | ----------------------------------------------------------------------------- | --------- |
| **Day 61** | Design `subscription` microservice schema (plans, features, quotas)           | 6h        |
| **Day 62** | Integrate Stripe products and plans (monthly/yearly tiers)                    | 6h        |
| **Day 63** | Webhook setup for Stripe events: `invoice.paid`, `subscription.updated`, etc. | 5h        |
| **Day 64** | Add API endpoints for listing plans, selecting a plan, updating plan          | 5h        |
| **Day 65** | Tenant ↔ Plan link logic, default plan for new tenants                        | 5h        |


🧾 Week 14: Billing & Stripe Checkout
| Day        | Tasks                                                           | Est. Time |
| ---------- | --------------------------------------------------------------- | --------- |
| **Day 66** | Stripe checkout integration (create checkout session, redirect) | 6h        |
| **Day 67** | Billing portal setup for managing payment methods/cancellations | 5h        |
| **Day 68** | Connect subscription plan to tenant's status and services       | 6h        |
| **Day 69** | Webhook tests with local tunneling (Stripe CLI or Ngrok)        | 5h        |
| **Day 70** | Finalize subscription UX flows (frontend + backend integration) | 5h        |


📊 Week 15: Usage Tracking Service
| Day        | Tasks                                                                | Est. Time |
| ---------- | -------------------------------------------------------------------- | --------- |
| **Day 71** | Build `usage` microservice (Mongo schema for logs, quotas)           | 5h        |
| **Day 72** | Track usage metrics: storage used, number of resources, team members | 6h        |
| **Day 73** | Add API to fetch current usage vs quota per tenant                   | 5h        |
| **Day 74** | Connect usage logic to feature lock/unlock by plan (e.g., max teams) | 6h        |
| **Day 75** | Write tests and setup alerts for quota breaches                      | 5h        |


🧩 Week 16: Feature Flags & Access Controls
| Day        | Tasks                                                           | Est. Time |
| ---------- | --------------------------------------------------------------- | --------- |
| **Day 76** | Build dynamic feature access middleware by plan level           | 6h        |
| **Day 77** | Add pricing tier map (e.g., Basic: 5 resources, Pro: unlimited) | 5h        |
| **Day 78** | Apply flags across services (studio, team, resources)           | 6h        |
| **Day 79** | Add admin override toggles for trial users or discounts         | 5h        |
| **Day 80** | QA for access restrictions and billing transitions              | 5h        |

🧑‍💼 Week 17: Customer Dashboard & Invoicing

| Day        | Tasks                                                               | Est. Time |
| ---------- | ------------------------------------------------------------------- | --------- |
| **Day 81** | Create `/billing` dashboard: current plan, usage, upgrade/downgrade | 6h        |
| **Day 82** | Add invoice history and download (Stripe links)                     | 5h        |
| **Day 83** | Email notifications for failed payments, quota limits               | 6h        |
| **Day 84** | Allow account cancellation and grace period handling                | 5h        |
| **Day 85** | Polish frontend flows for both free and paid users                  | 5h        |

🚀 Week 18: Final Integration & QA
| Day        | Tasks                                                         | Est. Time |
| ---------- | ------------------------------------------------------------- | --------- |
| **Day 86** | Full integration tests: signup → upgrade → downgrade → cancel | 6h        |
| **Day 87** | Backfill existing tenants with correct plan links             | 5h        |
| **Day 88** | Manual Stripe event simulation: renewal, failure, retries     | 5h        |
| **Day 89** | Fix bugs, improve logs and error handling                     | 6h        |
| **Day 90** | Deploy Phase 3 to staging/prod, tag and document release      | 5h        |


📊 Summary by Service (Phase 3)
| Component            | Est. Time |
| -------------------- | --------- |
| Subscription Core    | 27h       |
| Stripe Billing       | 27h       |
| Usage Tracking       | 27h       |
| Feature Access Logic | 27h       |
| Customer Dashboard   | 27h       |
| QA & Integration     | 27h       |
| **Total**            | \~162h    |


✅ Phase 4: Business-Specific & Cross-Cutting Services (Weeks 19–24)
Duration: 6 weeks
Goal: Build and deploy business-critical microservices plus infrastructure (API Gateway, Message Broker, Monitoring)

Week 19: Product & Inventory Service
| Day    | Tasks                                                          | Est. Time |
| ------ | -------------------------------------------------------------- | --------- |
| Day 91 | Design MongoDB schema for products, variants, stock, suppliers | 6h        |
| Day 92 | Implement CRUD APIs and variant management                     | 6h        |
| Day 93 | Build stock tracking, stock movement logic                     | 5h        |
| Day 94 | Add low stock alert event publishing                           | 5h        |
| Day 95 | Integrate event publishing to Message Broker                   | 5h        |

Week 20: POS (Point-of-Sale) Service
| Day     | Tasks                                                             | Est. Time |
| ------- | ----------------------------------------------------------------- | --------- |
| Day 96  | Design sales transaction schema, cashier roles                    | 6h        |
| Day 97  | Implement sales transactions, item scanning, discounts            | 6h        |
| Day 98  | Integrate with Product & Inventory service for stock verification | 5h        |
| Day 99  | Implement payment processing via gateway tokens                   | 5h        |
| Day 100 | Event publishing for completed sales                              | 5h        |


Week 21: Booking & Scheduling Service

| Day     | Tasks                                               | Est. Time |
| ------- | --------------------------------------------------- | --------- |
| Day 101 | Schema design for services, employees, appointments | 6h        |
| Day 102 | Implement booking API, availability calculations    | 6h        |
| Day 103 | Conflict detection and employee schedule management | 5h        |
| Day 104 | Publish booking events to Message Broker            | 5h        |
| Day 105 | Connect with CRM for customer details               | 5h        |

Week 22: CRM & Loyalty Service
| Day     | Tasks                                                   | Est. Time |
| ------- | ------------------------------------------------------- | --------- |
| Day 106 | Customer profile schema, loyalty points                 | 6h        |
| Day 107 | Purchase history ingestion from POS & Online Storefront | 6h        |
| Day 108 | Loyalty program logic and customer segmentation         | 5h        |
| Day 109 | Event consumption (Sales, Booking, Orders)              | 5h        |
| Day 110 | Customer creation and event publishing                  | 5h        |

Week 23: API Gateway & Message Broker Setup

| Day     | Tasks                                              | Est. Time |
| ------- | -------------------------------------------------- | --------- |
| Day 111 | Choose API Gateway (e.g., Kong) setup on Azure     | 6h        |
| Day 112 | Configure routing, JWT validation, rate limiting   | 6h        |
| Day 113 | Set up Message Broker (RabbitMQ/Kafka) in Azure    | 6h        |
| Day 114 | Connect microservices to message broker for events | 5h        |
| Day 115 | Test async communication and failover handling     | 5h        |


Week 24: Monitoring & Logging

| Day     | Tasks                                                                 | Est. Time |
| ------- | --------------------------------------------------------------------- | --------- |
| Day 116 | Set up Prometheus & Grafana or Azure Monitor                          | 6h        |
| Day 117 | Configure service metrics (CPU, memory, request rates)                | 5h        |
| Day 118 | Set up centralized log aggregation (ELK Stack or Azure Log Analytics) | 6h        |
| Day 119 | Implement alerting rules and dashboards                               | 5h        |
| Day 120 | Test monitoring, logging, and alert flows                             | 5h        |

Summary: Phase 4 Microservices and Infrastructure

| Service/Component            | Est. Hours |
| ---------------------------- | ---------- |
| Product & Inventory          | 27h        |
| POS Service                  | 27h        |
| Booking & Scheduling         | 27h        |
| CRM & Loyalty                | 27h        |
| API Gateway & Message Broker | 28h        |
| Monitoring & Logging         | 27h        |
| **Total**                    | \~163h     |
