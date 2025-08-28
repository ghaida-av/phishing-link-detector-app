import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(df, label_column='label', test_size=0.2, random_state=42):
    """
    Split dataset into train and test sets
    """
    train, test = train_test_split(df, test_size=test_size, stratify=df[label_column], random_state=random_state)
    return train, test

