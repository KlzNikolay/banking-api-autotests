from app.core.config import settings
import requests


class APIClient:

    def __init__(self):
        self.base_url = settings.api_base_url
        self.session = requests.Session()

    def get(self, endpoint: str):
        return self.session.get(f"{self.base_url}{endpoint}")

    def health(self):
        return self.get("/health")
