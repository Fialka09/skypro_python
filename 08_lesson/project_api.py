import requests
from config import BASE_URL, HEADERS, LOGIN, PASSWORD, COMPANY_ID


class ProjectAPI:

    def __init__(self):
        self.headers = HEADERS
        self.base_url = f"{BASE_URL}/projects"
        self.project_id = None

    def auth(self):
        """Получить токен по логину и паролю."""
        url = f"{BASE_URL}/auth/keys"
        data = {"login": LOGIN, "password": PASSWORD, "companyId": COMPANY_ID}
        response = requests.post(url, json=data)

        if response.status_code == 201:
            token = response.json()["key"]
            self.headers["Authorization"] = f"Bearer {token}"

        return response

    def create_project(self, title, users=None, departments=None):
        data = {"title": title}
        if users:
            data["users"] = users
        if departments:
            data["departments"] = departments

        response = requests.post(
            self.base_url, json=data, headers=self.headers
        )
        # Сохраняем ID созданного проекта для других методов
        if response.status_code == 201:
            self.project_id = response.json()["id"]

        return response

    def get_project(self, project_id=None):
        # Если ID не передан — берём сохранённый
        if project_id is None:
            project_id = self.project_id

        url = f"{self.base_url}/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(
        self,
        title,
        project_id=None,
        deleted=False,
        users=None,
        departments=None,
    ):
        if project_id is None:
            project_id = self.project_id

        url = f"{self.base_url}/{project_id}"
        data = {"title": title, "deleted": deleted}
        if users:
            data["users"] = users
        if departments:
            data["departments"] = departments

        return requests.put(url, json=data, headers=self.headers)
