from phish_detector.features import get_url_length, has_ip_address, get_domain

def test_url_length():
    assert get_url_length("http://example.com") == len("http://example.com")

def test_has_ip_address():
    assert has_ip_address("http://192.168.0.1/login") is True
    assert has_ip_address("http://example.com") is False

def test_get_domain():
    assert get_domain("http://example.com") == "example.com"

