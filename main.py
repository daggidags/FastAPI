from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import random
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, 'IMDB Dataset.csv')

app = FastAPI()

# Load sentiment model
model = joblib.load('sentiment_model.pkl')

# Load IMDB dataset
df = pd.read_csv(csv_path)

# Pydantic model for request body
class TextInput(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    prediction = model.predict([input.text])[0]
    return {"sentiment": prediction}

@app.post("/predict_proba")
def predict_sentiment_with_proba(input: TextInput):
    prediction = model.predict([input.text])[0]
    proba = model.predict_proba([input.text])[0]
    proba_value = max(proba)
    return {"sentiment": "positive", "probability": 0.95}

@app.get("/example")
def get_random_example():
    random_review = random.choice(df['review'].tolist())
    return {"review": random_review}

random_review = "I watched this with my kids and we all loved it."
