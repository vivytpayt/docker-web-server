import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv('DATABASE', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', '0.0.0.0')
DB_PORT = os.getenv('DB_PORT', 5432)
WEB_HOST = os.getenv('WEB_HOST', 'database')
WEB_PORT = os.getenv('WEB_PORT', 8080)
TABLE = os.getenv('TABLE', 'products')
