from fastapi import FastAPI
from phish_detector.model import load_model, predict

app = FastAPI(title="Phishing Detector API")

# Load model once when server starts
model = load_model()

@app.get("/")
def root():
    return {"message": "✅ Phishing Detector API is running"}

@app.post("/predict/")
def get_prediction(url: str):
    result = predict(model, url)
    return {"url": url, "prediction": result}
