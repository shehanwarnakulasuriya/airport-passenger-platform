import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "passengerdb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
        cursor_factory=RealDictCursor,
    )


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            passenger_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            flight VARCHAR(20) NOT NULL,
            status VARCHAR(30) NOT NULL
        );
    """)
    cur.execute("""
        INSERT INTO passengers (passenger_id, name, flight, status)
        VALUES
            ('P1001', 'Aroha Smith', 'NZ101', 'checked-in'),
            ('P1002', 'James Lee', 'NZ102', 'not-checked-in'),
            ('P1003', 'Mia Patel', 'NZ103', 'boarding')
        ON CONFLICT (passenger_id) DO NOTHING;
    """)
    conn.commit()
    cur.close()
    conn.close()
