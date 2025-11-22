import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    host='localhost',
    port=5432,
    database='hardware_store',
    user='postgres',
    password='postgres',
)

with connection:
    cursor = connection.cursor(cursor_factory=RealDictCursor)