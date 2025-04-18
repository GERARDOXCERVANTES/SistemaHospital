from src.config.config import DB_CONFIG
from src.service.database import Database

def get_db_connection():
    return Database(**DB_CONFIG)

