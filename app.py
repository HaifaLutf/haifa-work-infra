import os
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user="root",
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database="homelab_db"  # Pointing to your new database
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Fetch the logs you created in Step 1
        cursor.execute("SELECT id, event_name, created_at FROM logs ORDER BY created_at DESC")
        db_logs = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', logs=db_logs)
    except Exception as e:
        return f"<html><body><h1>Error</h1><p>{str(e)}</p></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
