
---

# Clinical Research Platform API

This is a REST API Project for managing clinical studies, sites, users (admins/subjects), and subject-submitted data. Built with Flask, RESTX, PostgreSQL, and JWT authentication.

---

## Features

- Admins can:
  - Create studies, sites, and users
  - View all subject data per site or study
- Subjects can:
  - Submit data to their assigned site
  - View data uploaded to their assigned site

---

## How to Run

### ✅ Local (without Docker)

1. **Clone the repo** and navigate into it
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the server:**

   ```bash
   python run
   ```
6. Swagger UI: [http://localhost:5000/swagger](http://localhost:5000/swagger)

---

## .env File

Create a `.env` file in the root folder:

```
JWT_SECRET_KEY=your-secret-key
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=db
DB_PORT=5432
DB_NAME=clinicaldb
```

---

### Docker Setup


1. Use above `.env` file
2. Run:

   ```bash
   docker-compose up --build
   ```
3. API will be live at: [http://localhost:5000](http://localhost:5000)



---

## API Endpoints

**All secured endpoints require a JWT token:**

```
Authorization: Bearer <access_token>
```

---

### Auth

| Method | URL         | Body                       | Description   |
| ------ | ----------- | -------------------------- | ------------- |
| POST   | /auth/login | { "username", "password" } | Get JWT token |

---

### Admin APIs

| Method | URL                            | Body/Params                                            | Description                  |
| ------ | ------------------------------ | ------------------------------------------------------ | ---------------------------- |
| POST   | /studies                       | { "name": "Study A" }                                  | Create a new study           |
| POST   | /sites                         | { "name": "Site X", "study\_id": 1 }                   | Create site in a study       |
| POST   | /users                         | { "name", "username", "password", "role", "site\_id" } | Create user                  |
| GET    | /sites/\<site\_id>/subjects    | –                                                      | List subjects at a site      |
| GET    | /subject-data/site/\<site\_id> | –                                                      | View subject data at a site  |
| GET    | /studies/\<study\_id>/subjects | –                                                      | List subjects across a study |

---

### Subject APIs

| Method | URL                            | Body                             | Description                    |
| ------ | ------------------------------ | -------------------------------- | ------------------------------ |
| POST   | /subject-data                  | { "data": "...", "site\_id": 2 } | Submit data to assigned site   |
| GET    | /subject-data/site/\<site\_id> | –                                | View data uploaded to own site |

---

## Testing

Use Postman or curl:

1. Authenticate via `/auth/login` to get a token.
2. Use the token in request headers like this:

```
Authorization: Bearer eyJhbGciOi...
```

---


