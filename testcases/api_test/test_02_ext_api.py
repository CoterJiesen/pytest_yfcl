import pytest
import allure
from operation.ext_api import push_ra_order_data, push_ra_bill_data
from operation.encode_api import get_core_company_sign, get_ra_encoded_data
from common.logger import logger
import operation.ext_api_data_init as datar
from common.conf import get_data
import json

conf_order = get_data("api_test_ext_order.yml")["test_push_order"]


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("外部接口测试模块-多个测试用例-配置模式")
@allure.feature("外部接口测试模块-多个测试用例-配置模式")
class TestExtApi:
    def setup_class(self):
        print("\nhere is setup_class")
        raDataItemsCount = conf_order["raDataItemsCount"]
        """构造核心企业数据"""
        logger.info("开始创建订单项，订单数 ==>>【 {} 】".format(raDataItemsCount))
        # 红色加力订单项
        self.ra_data_items = []
        for _ in range(raDataItemsCount):
            core_company_data = datar.create_core_company_data(
                datar.random_time("2023-04-01 00:00:00", "2023-04-05 23:00:00"),
                datar.random_time("2023-04-06 00:00:00", "2023-04-25 23:00:00"),
                datar.random_time("2023-04-25 00:00:00", "2023-04-29 23:00:00")
            )
            content = core_company_data.get("content")
            core_company_data["content"] = json.dumps(content, ensure_ascii=False)
            # print(core_company_data)
            # 获取签名
            result = get_core_company_sign(core_company_data)
            logger.info("code ==>> 核心企业签名，期望结果：0， 实际结果：【 {} 】".format(result["code"]))
            assert result["code"] == '0'
            logger.info("data ==>>【 {} 】，message ==>> 【 {} 】".format(result["data"], result["message"]))
            ra_data_item = datar.create_ra_data_item(content, result["data"])
            self.ra_data_items.append(ra_data_item)

    @allure.step("步骤2 ==>> 推送订单信息")
    def testPushRaOrderData(self):
        # 推送订单信息
        # 1、构造红色加力数据并获取加密结果
        totalBatch = conf_order["totalBatch"]
        currentBatch = conf_order["currentBatch"]
        logger.info("ra_data_items 长度 ==>> 【 {} 】".format(len(self.ra_data_items)))
        ra_data = datar.create_ra_data(totalBatch, currentBatch, self.ra_data_items)
        # print(ra_data)
        # 获取加密数据
        result = get_ra_encoded_data(ra_data)
        logger.info("code ==>> 【 {} 】".format(result["code"]))
        assert result["code"] == '0'
        logger.info("data ==>>【 {} 】，message ==>>【 {} 】".format(result["data"], result["message"]))

        # 2、加密结果发送给订单接口
        ra_encoded_data = result["data"]
        # print(ra_encoded_data)
        result = push_ra_order_data(ra_encoded_data)
        logger.info("result ==>> 【 {} 】".format(result))

    @allure.step("步骤3 ==>> 推送账单信息")
    def testPushRaBillData(self):
        """推送账单信息"""
        # 1、构造红色加力数据并获取加密结果
        logger.info("ra_data_items 长度 ==>> 【 {} 】".format(len(self.ra_data_items)))
        ra_data = datar.create_ra_bill_data(self.ra_data_items)
        # print(ra_data)
        # 获取加密数据
        result = get_ra_encoded_data(ra_data)
        logger.info("code ==>>【 {} 】".format(result["code"]))
        assert result["code"] == '0'
        logger.info("data ==>>【 {} 】，message ==>>【 {} 】".format(result["data"], result["message"]))

        # 2、加密结果发送给账单接口
        ra_encoded_data = result["data"]
        # print(ra_encoded_data)
        result = push_ra_bill_data(ra_encoded_data)
        logger.info("result ==>> 【 {} 】".format(result))


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_user_info.py"])
