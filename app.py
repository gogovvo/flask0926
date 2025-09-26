import os
from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)


DB_URI = os.getenv("DATABASE_URL")
engine = create_engine(DB_URI, pool_pre_ping=True)

@app.get("/")
def health():
    # DB 연결 테스트
    with engine.connect() as conn:
        v = conn.execute(text("SELECT 1")).scalar()
    return jsonify(ok=True, db=v)
