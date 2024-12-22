import json
from jsonschema import validate

# Load schema
with open("src/schemas/post_schema.json", "r") as schema_file:
    schema = json.load(schema_file)

# Example response data (adjust this to mimic your API's actual response)
response_data = [
    {
        "userId": 1,
        "id": 1,
        "title": "Post Title",
        "body": "Post Body"
    }
]

# Validate response against schema
try:
    validate(instance=response_data, schema=schema)
    print("Validation successful!")
except Exception as e:
    print(f"Validation error: {e}")
