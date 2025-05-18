import requests
from config import config

class BaseApi:
    def __init__(self):
        """Initialize the ApiBase class with configuration."""
        self.base_url = config.ENVIRONMENT.get("base_url")

    def get(self, endpoint, headers=None, params=None,data=None):
        """Perform a GET request."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers, params=params,data=data)
        return response

    def post(self, endpoint, headers=None, data=None, json=None):
        """Perform a POST request."""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=headers, data=data, json=json)
        return response

    def put(self, endpoint, headers=None, data=None, json=None):
        """Perform a PUT request."""
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=headers, data=data, json=json)
        return response

    def delete(self, endpoint, headers=None):
        """Perform a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response