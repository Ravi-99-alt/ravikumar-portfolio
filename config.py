
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.engine import URL


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from the project root
load_dotenv(BASE_DIR / ".env")


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-secret-key-change-before-deployment"
    )

    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="mysql+pymysql",

        username=os.getenv("MYSQL_USER"),

        password=os.getenv("MYSQL_PASSWORD"),

        host=os.getenv("MYSQL_HOST", "localhost"),

        port=int(os.getenv("MYSQL_PORT", "3306")),

        database=os.getenv("MYSQL_DATABASE", "portfolio_db"),

        query={
            "charset": "utf8mb4"
        }
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True
    }
