from data.post_payloads import UPDATE_POST_PAYLOAD


def test_update_existing_post(api_client, existing_post_id):
    response = api_client.put(f"/posts/{existing_post_id}", UPDATE_POST_PAYLOAD)
    updated_post = response.json()

    assert response.status_code == 200, "Expected status code 200 for an existing post"
    assert updated_post["id"] == existing_post_id, "Returned post ID should match the requested ID"
    assert updated_post["title"] == UPDATE_POST_PAYLOAD["title"], "Title was not updated correctly"
    assert updated_post["body"] == UPDATE_POST_PAYLOAD["body"], "The body was not updated correctly"