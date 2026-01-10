def test_delete_post(api_client, existing_post_id):
    response = api_client.delete(f"/posts/{existing_post_id}")
    assert response.status_code in (200, 204), "Expected 200 or 204 for delete operation"