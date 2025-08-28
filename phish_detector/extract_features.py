from phish_detector.features import get_url_length, has_ip_address, get_domain
from phish_detector.data_cleaning import clean_urls
import pandas as pd

def extract_features(df, url_column='url'):
    """
    Combine multiple URL features into a new dataframe
    """
    df = clean_urls(df, url_column=url_column)
    features = pd.DataFrame()
    features['url_len'] = df[url_column].apply(get_url_length)
    features['has_ip'] = df[url_column].apply(has_ip_address)
    features['domain'] = df[url_column].apply(get_domain)
    return features

