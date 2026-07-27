from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise RuntimeError("BASE_URL environment variable is required.")

try:
    TIMEOUT = int(os.getenv("TIMEOUT", 10))
except ValueError:
    raise RuntimeError("TIMEOUT must be an integer.")
