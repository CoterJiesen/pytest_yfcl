from api.ext_api import ext_api



def push_ra_order_data(data):
    """
    获取红色加力加密数据
    :param data:  红色加力数据
    :return: 返回内容
    """
    header = {
        "Content-Type": "application/json"
    }
    return ext_api.push_ra_order_data(json=data, headers=header)


def push_ra_bill_data(data):
    """
    获取红色加力加密数据
    :param data:  红色加力数据
    :return: 返回内容
    """
    header = {
        "Content-Type": "application/json"
    }
    return ext_api.push_ra_bill_data(json=data, headers=header)