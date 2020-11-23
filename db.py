from dotenv import load_dotenv
from orator import DatabaseManager, Schema, Model
import os

load_dotenv()

DATABASES = {
    "mysql": {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'blog',
        'user': os.getenv("DB_USERNAME"),
        'password': os.getenv("DB_PASSWORD"),
        'prefix': '',
        'port': 8889
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)