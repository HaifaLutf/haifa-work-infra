import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user="root",
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database="sys"
    )

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        return jsonify({"status": "Success", "message": "Connected to MySQL!"})
    except Exception as e:
        return jsonify({"status": "Error", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
