# API Automation Framework

This API Automation Framework is designed to streamline the testing of REST APIs using Python. It leverages `pytest` for testing, `requests` for HTTP requests, and other utilities for robust and scalable automation.

## Features

- Modular structure for easy scalability.
- Environment-based configuration management using `.env` files.
- Schema validation for API responses.
- Comprehensive test reports in HTML format.
- Centralized logging for better traceability.
- Support for parameterized testing with reusable test data.

## Project Structure

The framework is organized as follows:

- **`src/`**: Core source code.
  - `api_clients/`: Contains classes to interact with specific API endpoints.
  - `utils/`: Includes utility functions such as schema validation and request handling.
  - `schemas/`: JSON schema files for response validation.
  - `config.py`: Handles configuration settings like base URLs and environment variables.

- **`tests/`**: Test cases for validating API functionality.
  - `test_posts/`: Tests for post-related endpoints.
  - `regression_tests/`: Tests for regression scenarios.

- **`data/`**: Test data in JSON or CSV format for parameterized testing.

- **`reports/`**: Auto-generated test execution reports.

- **`logs/`**: Centralized log files for debugging and analysis.

- **`.env`**: Stores environment-specific variables (e.g., base URL, API keys).

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- `pip` (Python package manager)
- `virtualenv` (optional but recommended)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marcusqatech/api-automation-framework
   cd api-automation-framework
