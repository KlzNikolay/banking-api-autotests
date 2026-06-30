from app.core.config import settings
import requests


class APIClient:

    def __init__(self):
        self.base_url = settings.api_base_url
        self.session = requests.Session()

    def health(self):
        response = self.session.get(f"{self.base_url}/health")
        return response