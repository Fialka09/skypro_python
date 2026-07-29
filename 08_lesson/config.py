from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env в память

BASE_URL = "https://yougile.com/api-v2"
LOGIN = os.getenv("YOUGILE_LOGIN")
PASSWORD = os.getenv("YOUGILE_PASSWORD")
COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
TOKEN = os.getenv("YOUGILE_TOKEN")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}
