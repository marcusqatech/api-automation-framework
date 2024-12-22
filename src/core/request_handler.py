import requests
from src.core.logger import api_logger

class RequestHandler:
    @staticmethod
    def get(url, params=None):
        api_logger.info(f"GET Request to {url} with params {params}")
        response = requests.get(url, params=params)
        api_logger.info(f"Response: {response.status_code} - {response.json()}")
        return response

    @staticmethod
    def post(url, data=None):
        api_logger.info(f"POST Request to {url} with data {data}")
        response = requests.post(url, json=data)
        api_logger.info(f"Response: {response.status_code} - {response.json()}")
        return response
