import uuid

import pytest

from utils.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def existing_post_id(api_client):
    response = api_client.get("/posts")
    return response.json()[0]["id"]

@pytest.fixture
def not_existing_post_id():
    return uuid.uuid4()