import os
import jwt
import random
import pytest
import string
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app

load_dotenv()

SECRET = os.getenv("JWT_SECRET")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def random_prime():
    primes = [i for i in range(101) if is_prime(i)]
    return random.choice(primes)

def random_non_prime():
    non_primes = [i for i in range(101) if not is_prime(i)]
    return random.choice(non_primes)

def random_long_string():
    length = random.randint(257, 512)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_api(client):
    def _test_api(token):
        response = client.post("/validate_jwt", params={"input": token})
        return response.json()
    return _test_api

@pytest.fixture
def generate_token():
    def _generate_token(claims):
        return jwt.encode(claims, SECRET, algorithm="HS256")
    return _generate_token

@pytest.fixture
def generate_valid_claims():
    random_name = "".join(random.choices(string.ascii_letters, k=10))
    random_role = random.choice(["Admin", "Member", "External"])
    random_seed = random_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }

@pytest.fixture
def generate_invalid_claims():
    random_name = "".join(random.choices(string.ascii_letters, k=10))
    random_role = random.choice(["Admin", "Member", "External"])
    random_seed = random_non_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }

@pytest.fixture
def generate_invalid_seed():
    random_name = random_long_string()
    random_role = random.choice(["Admin", "Member", "External"])
    random_seed = random_non_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }

@pytest.fixture
def generate_invalid_name():
    random_name = random_long_string()
    random_role = random.choice(["admin", "member", "internal"])
    random_seed = random_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }

@pytest.fixture
def generate_invalid_name_number():
    random_name = random.choice(["Name123", 123456, "123456"])
    random_role = random.choice(["Admin", "Member", "External"])
    random_seed = random_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }

@pytest.fixture
def generate_invalid_role():
    random_name = "".join(random.choices(string.ascii_letters, k=10))
    random_role = random.choice(["admin", "member", "internal"])
    random_seed = random_prime()
    return {
        "Name": random_name,
        "Role": random_role,
        "Seed": random_seed
    }