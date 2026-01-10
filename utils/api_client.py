import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint, params=None):
        return requests.get(
            url=f"{self.BASE_URL}{endpoint}",
            params=params,
        )

    def post(self, endpoint, payload):
        return requests.post(
            url=f"{self.BASE_URL}{endpoint}",
            json=payload,
        )

    def put(self, endpoint, payload):
        return requests.put(
            url=f"{self.BASE_URL}{endpoint}",
            json=payload,
        )

    def delete(self, endpoint):
        return requests.delete(
            url=f"{self.BASE_URL}{endpoint}"
        )
