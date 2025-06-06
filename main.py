from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import openai
import os
import psycopg2
import time

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

model = joblib.load("model.pkl")

openai.api_key = os.getenv("OPENAI_API_KEY")

class QueryData(BaseModel):
    query: str
    table_size: int
    index_present: bool
    joins: int

@app.post("/predict")
def predict(data: QueryData):
    features = [[len(data.query), data.table_size, int(data.index_present), data.joins]]
    prediction = model.predict(features)[0]
    return {"classification": prediction}

@app.post("/suggest")
def suggest(data: QueryData):
    prompt = f"Optimize and explain this SQL query:
{data.query}
Table size: {data.table_size}, Index present: {data.index_present}, Joins: {data.joins}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"suggestion": response.choices[0].message.content}

@app.post("/execute")
def execute(data: QueryData):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT")
    )
    cursor = conn.cursor()
    start = time.time()
    cursor.execute(data.query)
    result = cursor.fetchall()
    elapsed = time.time() - start
    cursor.close()
    conn.close()
    return {"result": result, "execution_time": elapsed}
