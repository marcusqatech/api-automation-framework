import pytest
from src.api_clients.posts_client import PostsClient
from src.utils.schema_validator import validate_response_schema
import os


def test_get_single_post():
    post_id = 3
    # Send GET request to fetch a single post by ID
    response = PostsClient.get_post(post_id)
    assert response.status_code == 200
    schema_file = os.path.join(os.path.dirname(__file__), "../../src/schemas/post_schema.json")
    assert validate_response_schema(response, schema_file)
