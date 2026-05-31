import os
from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from db import get_connection, init_db

app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return jsonify({
        "service": "Airport Passenger Processing Platform API",
        "environment": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "1.0")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/passengers")
def passengers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers ORDER BY passenger_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/passengers/<passenger_id>")
def passenger(passenger_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE passenger_id = %s", (passenger_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        return jsonify({"error": "Passenger not found"}), 404
    return jsonify(row)

@app.route("/checkin/<passenger_id>", methods=["POST"])
def checkin(passenger_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE passengers SET status = %s WHERE passenger_id = %s RETURNING *",
        ("checked-in", passenger_id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if row is None:
        return jsonify({"error": "Passenger not found"}), 404
    return jsonify(row)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
