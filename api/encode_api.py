from core.rest_client import RestClient
from common.conf import get_data

host = get_data("env.yml")["host"]
active = host["active"]
api_root_url = host[active]["api_encode_url"]


class EncodeApi(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(EncodeApi, self).__init__(api_root_url, **kwargs)

    def get_core_company_sign(self, **kwargs):
        return self.post("/api/asset/external/getTestDataShop", **kwargs)

    def get_ra_encoded_data(self, **kwargs):
        return self.post("/api/asset/external/getTestData", **kwargs)


encodeApi = EncodeApi(api_root_url)
