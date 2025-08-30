from sklearn.model_selection import train_test_split
import pandas as pd

def split_dataset(df, test_size=0.2, label_column="label", random_state=42):
    # Handle very small datasets
    if len(df) < 2 or df[label_column].nunique() < 2:
        print("⚠️ Dataset too small or only one class. Returning all rows as train.")
        return df, pd.DataFrame(columns=df.columns)

    # Calculate test size as count, not just fraction
    test_count = int(len(df) * test_size)
    if test_count < df[label_column].nunique():
        print("⚠️ Not enough samples per class for stratify. Using random split instead.")
        return train_test_split(df, test_size=test_size, random_state=random_state)

    return train_test_split(
        df,
        test_size=test_size,
        stratify=df[label_column],
        random_state=random_state
    )

