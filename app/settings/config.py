from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.environ.get("DB_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
TOKEN_EXPIRY_IN_MINUTES = int(os.environ.get("TOKEN_EXPIRY_IN_MINUTES"))