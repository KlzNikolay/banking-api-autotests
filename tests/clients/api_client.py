from app.core.config import settings


class APIClient:

    def __init__(self):
        self.base_url = settings.api_base_url