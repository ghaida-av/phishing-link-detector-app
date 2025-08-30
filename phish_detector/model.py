import joblib

MODEL_PATH = "phish_detector/model.pkl"  # adjust if different

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, url: str):
    # TODO: Replace with your real feature extraction logic
    features = [len(url), url.count('.')]
    result = model.predict([features])[0]
    return "phishing" if result == 1 else "safe"
