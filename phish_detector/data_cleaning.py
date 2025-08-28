import pandas as pd

def clean_urls(df, url_column='url'):
    """
    Clean the URLs: strip spaces, lower case, remove empty strings
    """
    df[url_column] = df[url_column].astype(str).str.strip().str.lower()
    df = df[df[url_column] != ""].copy()
    df = df.drop_duplicates(subset=[url_column])
    return df

