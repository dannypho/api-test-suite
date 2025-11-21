import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL
    

def test_get_all_posts(base_url):
    """
    Test GET /posts endpoint returns all posts.
    Verifies status code 200 and response contains data.
    """
    r = requests.get(f"{base_url}/posts")

    assert r.status_code == 200
    assert len(r.json()) > 0

def test_get_single_post(base_url):
    """
    Test GET /posts/1 returns a specific post with correct structure.
    Verifies all required fields (userId, id, title, body) are present
    and the returned id matches the requested post.
    """
    r = requests.get(f"{base_url}/posts/1")
    data = r.json()

    assert r.status_code == 200
    assert 'userId' in data
    assert 'id' in data
    assert 'title' in data
    assert 'body' in data
    assert data['id'] == 1

def test_get_invalid_post(base_url):
    """
    Test GET /posts/999999 returns 404 for non-existent resource.
    Verifies proper error handling when requesting invalid post ID.
    """
    r = requests.get(f"{base_url}/posts/999999")

    assert r.status_code == 404
    assert len(r.json()) == 0

def test_get_posts_by_user(base_url):
    """
    Test GET /posts?userId=1 filters posts by specific user.
    Verifies query parameters work correctly and all returned
    posts belong to the specified userId.
    """
    payload = {'userId': 1}
    r = requests.get(f"{base_url}/posts", params=payload)

    data = r.json()

    assert r.status_code == 200
    assert len(data) > 0
    for post in data:
        assert post['userId'] == 1

def test_post_create_post(base_url):
    """
    Test POST /posts creates a new post.
    Verifies status code 201 (Created), response contains submitted
    data, and server assigns an id to the new post.
    """
    payload = {
        'title': 'Title of my test post',
        'body': 'Body of my test post',
        'userId': 1
    }

    r = requests.post(f"{base_url}/posts", json=payload)
    
    data = r.json()

    assert r.status_code == 201
    assert data['title'] == 'Title of my test post'
    assert data['body'] == 'Body of my test post'
    assert data['userId'] == 1
    assert 'id' in data

def test_put_update_post(base_url):
    """
    Test PUT /posts/1 updates an existing post.
    Verifies status code 200 and response reflects the updated data.
    """
    payload = {
        'id': 1,
        'title': 'Updated title',
        'body': 'Updated body',
        'userId': 1
    }

    r = requests.put(f"{base_url}/posts/1", json=payload)

    data = r.json()

    assert r.status_code == 200
    assert data['id'] == 1
    assert data['title'] == 'Updated title'
    assert data['body'] == 'Updated body'
    assert data['userId'] == 1

def test_delete_post(base_url):
    """
    Test DELETE /posts/1 removes a post successfully.
    Verifies status code 200 and response indicates successful deletion.
    """
    r = requests.delete(f"{base_url}/posts/1")

    data = r.json()

    assert r.status_code == 200
    assert len(data) == 0

def test_response_headers(base_url):
    """
    Test API responses contain correct headers.
    Verifies Content-Type header is set to application/json.
    """
    r = requests.get(f"{base_url}/posts")
    
    assert r.status_code == 200
    assert 'application/json' in r.headers['Content-Type']

def test_response_schema(base_url):
    """
    Test response structure includes all required fields with correct data types.
    Verifies userId and id are integers, title and body are strings.
    """
    r = requests.get(f"{base_url}/posts/1")

    data = r.json()

    assert r.status_code == 200
    assert 'id' in data
    assert 'userId' in data
    assert 'body' in data
    assert 'title' in data
    assert isinstance(data['userId'], int)
    assert isinstance(data['id'], int)
    assert isinstance(data['body'], str)
    assert isinstance(data['title'], str)

def test_response_time(base_url):
    """
    Test API response time meets performance requirements.
    Verifies response returns within 2 seconds.
    """
    r = requests.get(f"{base_url}/posts")
    response_time = r.elapsed.total_seconds()

    assert r.status_code == 200
    assert response_time < 2