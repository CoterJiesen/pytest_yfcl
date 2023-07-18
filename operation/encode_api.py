from api.encode_api import encodeApi
from common.conf import get_token


def get_core_company_sign(core_data):
    """
    获取核心企业原始数据签名
    :param core_data:  核心企业原始数据
    :return: 返回内容
    """
    header = {
        "Content-Type": "application/json"
    }
    token = get_token()
    if token:
        header["token"] = token
    response = encodeApi.get_core_company_sign(json=core_data, headers=header)
    assert response.status_code == 200
    return response.json()


def get_ra_encoded_data(data):
    """
    获取红色加力加密数据
    :param data:  红色加力数据
    :return: 返回内容
    """
    header = {
        "Content-Type": "application/json"
    }
    response = encodeApi.get_ra_encoded_data(json=data, headers=header)
    assert response.status_code == 200
    return response.json()
