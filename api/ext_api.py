from core.rest_client import RestClient
from common.conf import get_data
from common.logger import logger

host = get_data("env.yml")["host"]
active = host["active"]
api_root_url = host[active]["open_gateway_url"]
pass_gateway = host["pass_gateway"]


class ExtApi(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(ExtApi, self).__init__(api_root_url, **kwargs)

    def push_ra_order_data(self, **kwargs):
        response = self.post("/api/asset/external/pushOrderInfo", **kwargs)
        assert response.status_code == 200
        json = response.json()
        logger.info(json)
        # 不经过网关
        if pass_gateway == 0:
            assert json["code"] == '0'
            assert json["data"]["code"] == '1'
        else:
            # 经过网关
            assert json["code"] == '1'
        return json

    def push_ra_bill_data(self, **kwargs):
        response = self.post("/api/asset/external/pushBillInfo", **kwargs)
        assert response.status_code == 200
        json = response.json()
        logger.info(json)
        # 不经过网关
        if pass_gateway == 0:
            assert json["code"] == '0'
            assert json["data"]["code"] == '1'
        else:
            # 经过网关
            assert json["code"] == '1'
        return json


ext_api = ExtApi(api_root_url)