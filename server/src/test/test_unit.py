import app
import pytest
from requests import get, post
from pydantic import BaseModel, Field, EmailStr, HttpUrl, validator


BASE_URL = "http://localhost"

def endpoint(path):                         
    return f"{BASE_URL}{path}"

"""

Tests to validate OAuth2 authentication flow for Client Token (IdToken) and M2M Token (AccessToken)
"""

auth_endpoints = ['/','/token/{token}']

@pytest.mark.dependency()
def test_get_token():
    e = endpoint('/')
    r = get(e)
    assert r.status_code == 200

def test_verify_token(depends=[test_get_token]):
    e = endpoint(f'/token/{test_get_token()}')
    r = get(e)
    assert r.status_code == 200