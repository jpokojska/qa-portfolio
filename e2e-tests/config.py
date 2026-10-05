import os

from dotenv import load_dotenv

load_dotenv()

# Defaults are the public Restful-Booker Platform demo values.
# Override them with environment variables or a .env file (see .env.example).
BASE_URL = os.getenv("BASE_URL", "http://localhost:3003")
BOOKING_URL = os.getenv("BOOKING_URL", "http://localhost:3000")
AUTH_URL = os.getenv("AUTH_URL", "http://localhost:3004")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "password")
