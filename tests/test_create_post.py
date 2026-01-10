from data.post_payloads import VALID_CREATE_POST_PAYLOAD, INVALID_CREATE_POST_PAYLOAD

EXPECTED_FIELDS = {"id", "title", "body", "userId"}

def test_create_post_with_valid_payload(api_client):
    response = api_client.post("/posts", VALID_CREATE_POST_PAYLOAD)
    post = response.json()
    assert response.status_code == 201 , "Expected 201 for created post"
    assert EXPECTED_FIELDS.issubset(post.keys()), "Response should contain expected fields"

def test_create_post_with_invalid_payload(api_client):
    response = api_client.post("/posts", INVALID_CREATE_POST_PAYLOAD)

    # JSONPlaceholder is a fake API and does not enforce payload validation.
    # This test verifies the observed behavior rather than expecting a 4xx.
    assert response.status_code == 201, "JSONPlaceholder returns 201 even for incomplete payloads"