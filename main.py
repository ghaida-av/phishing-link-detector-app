import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from phish_detector.features import extract_features

app = FastAPI()

# Load ML pipeline
model = joblib.load("phish_detector/pipeline.joblib")

class URLItem(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "✅ Phishing Detector API is running"}

@app.post("/predict/")
def predict(item: URLItem):
    url = item.url
    features = extract_features(url)
    prediction = model.predict([features])[0]
    return {"url": url, "prediction": int(prediction)}


