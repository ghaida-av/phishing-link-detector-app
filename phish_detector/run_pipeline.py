import pandas as pd
from phish_detector.data_cleaning import clean_urls
from phish_detector.data_split import split_dataset
from phish_detector.extract_features import extract_features

# Load dataset
df = pd.read_csv("data/raw/example_urls.csv")

# Clean URLs
df_clean = clean_urls(df)

# Split dataset
train, test = split_dataset(df_clean)

# Extract features
train_features = extract_features(train)
test_features = extract_features(test)

# Save processed files
train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)
train_features.to_csv("data/processed/train_features.csv", index=False)
test_features.to_csv("data/processed/test_features.csv", index=False)

print("Pipeline completed successfully!")
print(f"Train samples: {len(train)}, Test samples: {len(test)}")
