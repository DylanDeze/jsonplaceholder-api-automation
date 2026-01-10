def test_get_all_posts(api_client):

    response = api_client.get("/posts")
    all_posts = response.json()
    keys = {'userId', 'id', 'title', 'body'}

    assert response.status_code == 200
    assert isinstance(all_posts, list), \
        "All posts should be a list"
    assert all_posts != [], \
        "All posts must not be empty"
    assert all(keys.issubset(post) for post in all_posts), \
        "Some posts are missing required keys"

def test_get_existing_post_by_id(api_client, existing_post_id):
    response = api_client.get(f"/posts/{existing_post_id}")

    assert response.status_code == 200, \
        "Expected status code 200 for an existing post"
    assert response.json()["id"] == existing_post_id, \
        "Returned post ID should match the requested ID"

def test_get_not_existing_post_by_id(api_client, not_existing_post_id):
    response = api_client.get(f"/posts/{not_existing_post_id}")

    assert response.status_code == 404 , \
        "Expected 404 for non existing post"
