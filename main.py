from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# ✅ Allow frontend (phish-front) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now allow all, you can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model
try:
    model = joblib.load("phish_detector/pipeline.joblib")
except:
    model = None

class URLItem(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "✅ Phishing Detector API is running"}

@app.post("/predict/")
def predict(item: URLItem):
    if not model:
        return {"error": "Model not loaded"}
    prediction = model.predict([item.url])[0]
    return {"url": item.url, "prediction": prediction}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





