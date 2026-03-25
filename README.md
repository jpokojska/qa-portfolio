# QA Portfolio — Restful-Booker Platform

![Playwright Tests](https://github.com/YOUR_USERNAME/qa-portfolio/actions/workflows/playwright-tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Playwright](https://img.shields.io/badge/playwright-latest-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal QA portfolio project demonstrating API and E2E test automation skills using industry-standard tools and patterns.

---

## 🧪 What's tested

**Target application:** [Restful-Booker Platform](https://automationintesting.online) — a hotel booking demo app running locally via Docker.

| Area | Tool | Tests |
|------|------|-------|
| REST API | Postman + Newman | ~15 requests |
| Frontend E2E | Playwright + Python | ~8 scenarios |

---

## 🗂️ Project structure

```
qa-portfolio/
├── api-tests/
│   └── postman/
│       ├── restful-booker.postman_collection.json
│       └── environments/
│           └── local.postman_environment.json
└── e2e-tests/
    ├── pages/               # Page Object Model
    │   ├── booking_page.py
    │   ├── admin_login_page.py
    │   └── admin_dashboard_page.py
    ├── tests/
    │   ├── test_booking.py
    │   └── test_admin.py
    ├── conftest.py
    ├── requirements.txt
    └── playwright.config.py
```

---

## 🚀 Running locally

### Prerequisites
- Docker Desktop
- Python 3.11+
- Node.js (for Newman — optional, for Postman CLI runs)

### 1. Start the application

```bash
docker run -d \
  --name restful-booker \
  -p 3000:3000 \
  mwinteringham/restfulbooker-platform
```

App will be available at `http://localhost:3000`

### 2. Run E2E tests

```bash
cd e2e-tests
pip install -r requirements.txt
playwright install chromium
pytest --html=report.html
```

### 3. Run API tests (Newman)

```bash
cd api-tests
npm install -g newman newman-reporter-htmlextra
newman run postman/restful-booker.postman_collection.json \
  -e postman/environments/local.postman_environment.json \
  --reporters cli,htmlextra
```

---

## 📋 Test scenarios

### API Tests (Postman)
- `POST /auth` — generate auth token
- `GET /booking` — list all bookings
- `GET /booking/{id}` — get booking by ID
- `POST /booking` — create booking (positive + negative)
- `PUT /booking/{id}` — update booking (auth required)
- `DELETE /booking/{id}` — delete booking (auth required)

### E2E Tests (Playwright)
- ✅ Guest can submit a booking request
- ✅ Booking form validation — required fields
- ✅ Admin can log in with valid credentials
- ❌ Admin login fails with invalid credentials
- ✅ Admin sees booking list on dashboard
- ✅ Admin can delete a booking
- ✅ Room details are displayed correctly
- ❌ Booking fails when dates are in the past

---

## 🔁 CI/CD

Tests run automatically on every push via **GitHub Actions**.
Playwright HTML report is published as a workflow artifact after each run.

---

## 🛣️ Future improvements

- [ ] Visual regression tests (Playwright screenshots)
- [ ] Performance tests (k6)
- [ ] Data-driven tests with fixtures
- [ ] Mobile viewport coverage
- [ ] Full Docker Compose setup (app + test runner)
- [ ] Allure report integration

---

## 👤 Author

**Your Name**
[LinkedIn](https://linkedin.com/in/yourprofile) · [GitHub](https://github.com/YOUR_USERNAME)
