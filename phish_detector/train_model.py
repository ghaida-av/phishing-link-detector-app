# phish_detector/train_model.py
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from phish_detector.features import extract_features

# Dummy dataset
data = {
    "url": [
        "http://google.com",
        "http://facebook.com",
        "http://paypal.com",
        "http://malicious-site.ru/bad",
        "http://login-phish.com/steal",
    ],
    "label": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

# Extract features for each URL
X = df["url"].apply(extract_features)
y = df["label"]

# Define pipeline: DictVectorizer + LogisticRegression
pipeline = Pipeline([
    ("vectorizer", DictVectorizer(sparse=False)),
    ("classifier", LogisticRegression())
])

# Train the model
pipeline.fit(X, y)

# Save pipeline
joblib.dump(pipeline, "phish_detector/pipeline.joblib")
print("✅ Feature-based model trained and saved")



