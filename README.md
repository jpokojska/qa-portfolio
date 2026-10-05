# QA Portfolio — Restful-Booker Platform

![QA Tests](https://github.com/jpokojska/qa-portfolio/actions/workflows/playwright-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Playwright](https://img.shields.io/badge/playwright-1.49.1-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal QA portfolio project demonstrating API and E2E test automation skills using industry-standard tools and patterns.

---

## 🧪 What's tested

**Target application:** [Restful-Booker Platform](https://automationintesting.online) — a hotel booking system running locally.

| Area | Tool | Tests |
|------|------|-------|
| REST API | Postman + Newman | 9 requests |
| Frontend E2E | Playwright + Python | 4 scenarios |

---

## 🗂️ Project structure

```
qa-portfolio/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml    # CI/CD pipeline (API + E2E)
├── api-tests/
│   └── postman/
│       ├── Restful-Booker-Platform.postman_collection.json
│       └── environments/
│           └── local.postman_environment.json
└── e2e-tests/
    ├── pages/                      # Page Object Model
    │   ├── admin_login_page.py
    │   ├── home_page.py
    │   └── reservation_page.py
    ├── tests/
    │   ├── test_admin.py
    │   └── test_reservation.py
    ├── conftest.py
    └── requirements.txt
```

---

## 🚀 Running locally

### Prerequisites
- Java JDK 21+
- Maven 3.6.3+
- Node.js 22+
- Python 3.11+

### 1. Clone and start Restful-Booker Platform

```bash
git clone https://github.com/mwinteringham/restful-booker-platform.git
cd restful-booker-platform
bash build_locally.sh
```

Application will be available at:
- **Frontend:** `http://localhost:3003`
- **Booking API:** `http://localhost:3000`
- **Auth API:** `http://localhost:3004`

### 2. Run E2E tests

```bash
cd e2e-tests
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v
```

URLs and admin credentials are read from environment variables in `e2e-tests/config.py`. Defaults are the public Restful-Booker Platform demo values (`admin` / `password`), so tests run out of the box. To test against a different environment, copy `e2e-tests/.env.example` to `e2e-tests/.env` and adjust the values.

### 3. Run API tests (Postman)

1. Import `api-tests/postman/Restful-Booker-Platform.postman_collection.json` into Postman
2. Import `api-tests/postman/environments/local.postman_environment.json`
3. Set **Current Value** for environment variables:
   - `base_url`: `http://localhost:3000`
   - `auth_url`: `http://localhost:3004`
   - `username` / `password` are prefilled with the public demo credentials (`admin` / `password`)
4. Select `local` environment and run the collection

Or run the collection from the command line with [Newman](https://github.com/postmanlabs/newman) (requires Node.js):

```bash
npx newman run api-tests/postman/Restful-Booker-Platform.postman_collection.json \
  -e api-tests/postman/environments/local.postman_environment.json \
  --env-var base_url=http://localhost:3000 \
  --env-var auth_url=http://localhost:3004
```

---

## 📋 Test scenarios

### API Tests (Postman)

**Auth**
- `POST /auth/login` — valid credentials, token saved to environment
- `POST /auth/login` — invalid credentials, returns 403

**Bookings**
- `GET /booking/` — list all bookings
- `GET /booking/{id}` — get single booking by ID
- `POST /booking/` — create booking, ID saved to environment
- `PUT /booking/{id}` — update booking
- `DELETE /booking/{id}` — delete booking
- `POST /booking/` — missing required fields, returns 400
- `DELETE /booking/{id}` — booking not found, returns 404

### E2E Tests (Playwright)

**Admin**
- ✅ Admin can log in with valid credentials
- ✅ Admin login fails with invalid credentials

**Reservation**
- ✅ Guest can book a room — happy path
- ✅ Booking form validation — submit without required fields

---

## 🔁 CI/CD

Tests run automatically on every push and pull request to `main` via **GitHub Actions**.

Pipeline steps:
1. Checkout repository
2. Setup Java 26, Node.js 22, Python 3.11
3. Build and start Restful-Booker Platform
4. Install Playwright + Chromium
5. Run API tests (Postman collection via Newman)
6. Run E2E tests (Playwright) — runs even if API tests fail, so both results are visible
7. Upload reports as artifact (`test-reports`: Newman JUnit XML, Playwright HTML report, trace, app log)

---

## 🛣️ Future improvements

### Tests
- [ ] Admin dashboard tests (delete booking, manage rooms)
- [ ] Visual regression tests (Playwright screenshots)

### Code quality
- [ ] Standardize locators — migrate all to `get_by_role()` / `get_by_label()`
- [ ] Add Faker library for dynamic test data generation
- [x] Extract hardcoded URLs and credentials to `.env` file
- [ ] Add base Page Object class with common methods

### Reporting & CI
- [ ] Allure report integration
- [x] Newman runner for Postman collection in CI

---

## 👤 Author

**Joanna Pokojska**
[GitHub](https://github.com/jpokojska)
