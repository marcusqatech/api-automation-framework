import pytest
from src.api_clients.posts_client import PostsClient
from src.utils.schema_validator import validate_response_schema
import os

def test_get_all_posts():
    # Send GET request to fetch all posts
    response = PostsClient.get_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    schema_file = os.path.join(os.path.dirname(__file__), "../../src/schemas/post_schema.json")
    assert validate_response_schema(response, schema_file)
    #print(response.json())


