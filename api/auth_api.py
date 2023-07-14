from core.rest_client import RestClient
from common.conf import get_data
from common.logger import logger

host = get_data("env.yml")["host"]
active = host["active"]
api_root_url = host[active]["gateway_url"]


class UserApi(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(UserApi, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        response = self.post("/api/authcenter/login", **kwargs)
        assert response.status_code == 200
        json = response.json()
        logger.info(json)
        assert json["code"] == '0'
        return json


auth = UserApi(api_root_url)
