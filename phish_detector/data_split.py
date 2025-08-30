from sklearn.model_selection import train_test_split

def split_dataset(df, label_column="label", test_size=0.2, random_state=42):
    if df[label_column].nunique() < 2 or len(df) < 5:
        print("⚠️ Dataset too small for stratified split. Returning full dataset as train, empty test.")
        return df, df.iloc[0:0]  # all train, no test
    
    return train_test_split(
        df,
        test_size=test_size,
        stratify=df[label_column],
        random_state=random_state
    )


