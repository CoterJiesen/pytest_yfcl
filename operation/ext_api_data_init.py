import datetime
import random
import time
import json
from common.conf import get_data

test_push_order = get_data("api_test_ext_order.yml")["test_push_order"]
company = test_push_order["company"]
assetProvider = company["assetProvider"]
coreCompany = company["coreCompany"]


def random_times(start, end, n, frmt="%Y-%m-%d %H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime = [random.random() * (etime - stime) + stime for _ in range(n)]
    time_str = [t.strftime(frmt) for t in time_datetime]
    return time_str


def random_time(start, end, frmt="%Y-%m-%d %H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime = random.random() * (etime - stime) + stime
    # 返回格式化的时间字符串
    # return time_datetime.strftime(frmt)
    # 返回时间戳毫秒数
    return int(time_datetime.timestamp() * 1000)


def create_core_company_data(checkInDate, checkOutDate, saleDate):
    """
    构造随机核心企业数据
    """
    hotels = ['万豪', '洲际', '希尔顿', '如家', '7天', '格林', '全季', '亚朵', '维也纳酒店', '锦江之星']
    core_company_data = {
        "orderNo": "HXQY_" + str(int(time.time())) + str(random.randint(1000, 9999)),
        "hotelName": hotels[random.randint(0, len(hotels) - 1)] + str(random.randint(1000, 9999)),
        "hotelCode": "HTCODE_" + str(random.randint(1000, 9999)),
        "coreCompanyName": coreCompany["coreCompanyName"],
        "coreCompanyCertNo": coreCompany["coreCompanyCertNo"],
        "roomNum": random.randint(1, 100),
        "saleDate": saleDate,
        "checkInDate": checkInDate,
        "checkOutDate": checkOutDate,
        "orderAmount": {
            "amount": 100 * random.randint(100, 1000),
            "currency": "CNY"
        }
    }
    return {
        "content": core_company_data,
        "companyCertNo": coreCompany["coreCompanyCertNo"]
    }


def create_ra_data_item(core_company_data, signature):
    ra_data_item = core_company_data.copy()
    ra_data_item["raOrderNo"] = core_company_data.get("orderNo")
    ra_data_item["amount"] = core_company_data.get("orderAmount").get("amount")
    ra_data_item["currency"] = core_company_data.get("orderAmount").get("currency")
    ra_data_item["originalData"] = json.dumps(core_company_data, ensure_ascii=False)
    ra_data_item["orderSignture"] = signature
    ra_data_item.pop("orderAmount")
    ra_data_item.pop("orderNo")
    return ra_data_item


def create_ra_data(totalBatch, currentBatch, ra_data_items):
    ra_data = {
        "assetProviderName": assetProvider["assetProviderName"],
        "assetProviderCertNo": assetProvider["assetProviderCertNo"],
        "coreCompanyName": coreCompany["coreCompanyName"],
        "coreCompanyCertNo": coreCompany["coreCompanyCertNo"],
        "totalBatch": totalBatch,
        "currentBatch": currentBatch,
        "list": ra_data_items
    }
    return ra_data


def create_ra_bill_data(ra_data_items):
    billAmt = 0
    orderInfos = []
    for i in range(len(ra_data_items)):
        billAmt += ra_data_items[i]["amount"]
        orderInfos.append({
            "raOrderNo": ra_data_items[i]["raOrderNo"],
            "paidAmt": ra_data_items[i]["amount"]
        })

    bill_data = {
        "billInfo": {
            "billStatus": "1",
            "coreCompanyName": coreCompany["coreCompanyName"],
            "coreCompanyCertNo": coreCompany["coreCompanyCertNo"],
            "billNo": "BILL_" + str(int(time.time())) + str(random.randint(1000, 9999)),
            "billDate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "billAmt": billAmt,
            "orderInfo": orderInfos
        }
    }
    return bill_data
