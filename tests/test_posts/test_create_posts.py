import pytest
from src.api_clients.posts_client import PostsClient
from src.data_providers.post_data_provider import get_post_data
from src.utils.schema_validator import validate_response_schema
import os

@pytest.mark.parametrize("post_data", get_post_data())
def test_create_post(post_data):
    # Step 1: Send POST request with test data
    response = PostsClient.create_post(post_data)

    # Step 2: Validate status code
    assert response.status_code == 201

    # Step 3: Define the schema file for validation
    schema_file = os.path.join(os.path.dirname(__file__), "../../src/schemas/post_schema.json")

    # Step 4: Validate the response JSON structure
    #assert validate_response_schema(response, schema_file)

    # Step 5: Validate specific fields in the response
    assert response.json()["title"] == post_data["title"]
