import httpx
import pytest

BASE_URL="http://127.0.0.1:8000"

@pytest.fixture
def register_user():
    httpx.post(
        f"{BASE_URL}/register",
        json={
            "email":"test@gmail.com",
            "password":"123"
        }
    )
 


def test_login_success(register_user):
    response=httpx.post(
        f"{BASE_URL}/login",
        json={
             "email":"test@gmail.com",
            "password":"123"
        }
    )
    assert response.status_code==200
    assert response.json()["message"]=="Login successful"

def test_login_wrong_password(register_user):
    response=httpx.post(
        f"{BASE_URL}/login",
        json={
            "email":"test@gmail.com",
            "password":"1234"
        }
    )
    assert response.json()["message"]=="Invalid credentials"


def test_login_user_not_found():
    response=httpx.post(
        f"{BASE_URL}/login",
        json={
              "email":"unknown@gmail.com",
              "password":"12345"
        }
    )
    assert response.json()["message"]=="User not found"