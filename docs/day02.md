
## ✅ Day 02 – FFMint: Scaffold & Integrate Storage Service (FastAPI + Azure Blob Storage)

- [ ] 🔹 **Scaffold Storage Service (FastAPI)**
  - Create a new FastAPI service folder with structure like `routers/`, `schemas/`, `services/`, `config/`
  - Mirror structure from your IAM service (if already done)
  - [📺 Tutorial: Scalable FastAPI Project Structure](https://www.youtube.com/watch?v=0sOvCWFmrtA)

- [ ] 🔹 **Add `/upload`, `/download`, and `/presign` route placeholders**
  - Implement placeholder endpoints in `routers/storage.py`
  - Define request/response models in `schemas/storage.py`
  - Wire up routing in `main.py`
  - [📺 Tutorial: FastAPI Routing & Dependency Injection](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=925s)

- [ ] 🔹 **Add dummy Azure Blob Storage integration (locally)**
  - Set up local `.env` for Azure connection string
  - Use `azure-storage-blob` SDK to interact with Azure Blob Storage
  - Create dummy upload/download/presigned URL logic in `services/storage.py`
  - [📺 Tutorial: FastAPI + Azure Blob Storage Upload](https://www.youtube.com/watch?v=KsT-y9F-JB8)
  - [📺 Bonus: Azure Blob Storage Python SDK Basics](https://www.youtube.com/watch?v=2JrD5k2Z-Ps)

- [ ] 🔹 **Add placeholders for Azure DevOps pipeline integration**
  - Set up service-level `Dockerfile` and `requirements.txt`
  - Add Azure DevOps `azure-pipelines.yml` placeholder for CI/CD
  - [📺 Tutorial: Azure DevOps CI/CD for FastAPI Docker Apps](https://www.youtube.com/watch?v=mJ4XTtG5nE8)




Day 2: Implement JWT Token Handling and Secure Routes
Objective: Implement JSON Web Token (JWT) based authentication, including access and refresh tokens, and secure API routes using middleware and dependency injection.

Time Allotment: 5 hours

Key Tasks:

Implement JWT Token Handling (Access/Refresh): Develop the logic for generating, signing, and verifying both access and refresh JWT tokens.
Add Middleware to Validate JWT: Create a middleware function that intercepts incoming requests, extracts the JWT, validates its authenticity and expiry, and attaches user information to the request object.
Secure Routes via Dependency Injection: Integrate the JWT validation middleware into protected routes, likely by injecting it as a dependency, to ensure only authenticated requests can access them.
Actionable Plan:

Token Generation Logic (1.5 hours):

Define JWT payload structure (user ID, roles, expiry).
Implement functions to generate access tokens with short expiry.
Implement functions to generate refresh tokens with longer expiry.
Securely store JWT secrets (environment variables).
JWT Validation Middleware (2 hours):

Create a new middleware function (e.g., authenticateJWT).
Extract JWT from Authorization header.
Use a JWT library to verify the token's signature and expiry.
Handle invalid or expired tokens (e.g., return 401 Unauthorized).
If valid, decode the token and attach user information to the request object (req.user = decoded_payload).
Route Protection via Dependency Injection (1.5 hours):

Identify routes that require authentication.
Apply the authenticateJWT middleware to these routes.
For frameworks supporting dependency injection, inject the middleware into the route definitions or controllers.
Test secured routes with and without valid tokens.
Checklist:

[ ] JWT secret securely configured (e.g., in .env file).
[ ] Function to generate access token implemented.
[ ] Function to generate refresh token implemented.
[ ] JWT validation middleware created.
[ ] Middleware successfully extracts token from Authorization header.
[ ] Middleware correctly verifies JWT signature.
[ ] Middleware handles token expiry.
[ ] User information attached to request object after successful validation.
[ ] Selected routes are protected by the JWT middleware.
[ ] Unauthenticated access to protected routes returns 401.
[ ] Authenticated access to protected routes is successful.
[ ] Refresh token mechanism tested (if applicable for immediate implementation).
