import pytest
import pandas as pd
from phish_detector.data_split import split_dataset

def test_split_dataset_small_data():
    df = pd.DataFrame({"url": ["a", "b"], "label": [0, 1]})
    train, test = split_dataset(df)
    assert len(train) > 0
    assert "label" in train.columns
