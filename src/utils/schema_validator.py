import json
from jsonschema import validate, ValidationError

def validate_response_schema(response, schema_file):
    try:
        with open(schema_file, "r") as file:
            schema = json.load(file)
        validate(instance=response.json(), schema=schema)
        return True
    except ValidationError as e:
        print(f"Schema validation error: {e}")
        return False
    except Exception as e:
        print(f"Error loading schema: {e}")
        return False
