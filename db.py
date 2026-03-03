# db.py — Shared database connection utility
# Every script in the project imports from here.

import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import logging

load_dotenv()  # This reads your .env file

logger = logging.getLogger(__name__)

def get_engine():
    """
    Creates and returns a SQLAlchemy database engine.
    Reads connection details from environment variables.
    """
    db_url = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return create_engine(db_url)

def test_connection():
    """
    Simple test to verify the database is reachable.
    Run this script directly to confirm setup is working.
    """
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM stocks"))
            count = result.scalar()
            print(f"Connection successful. Stocks table has {count} rows.")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()