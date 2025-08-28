from phish_detector.features import get_url_length, has_ip_address, get_domain
from phish_detector.data_cleaning import clean_urls
from phish_detector.extract_features import extract_features
import pandas as pd

def test_url_length():
    assert get_url_length("http://example.com") == len("http://example.com")

def test_has_ip_address():
    assert has_ip_address("http://192.168.0.1/login") is True
    assert has_ip_address("http://example.com") is False

def test_get_domain():
    assert get_domain("http://example.com") == "example.com"

def test_clean_urls():
    df = pd.DataFrame({'url': [' HTTP://EXAMPLE.COM ', '', 'http://test.com']})
    cleaned = clean_urls(df)
    assert len(cleaned) == 2
    assert all(cleaned['url'] == ['http://example.com', 'http://test.com'])

def test_extract_features():
    df = pd.DataFrame({'url': ['http://example.com', 'http://192.168.0.1']})
    feats = extract_features(df)
    assert 'url_len' in feats.columns
    assert 'has_ip' in feats.columns
    assert 'domain' in feats.columns


