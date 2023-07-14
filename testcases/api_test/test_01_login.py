import pytest
import allure
from common.logger import logger
from common.conf import get_data

conf_order = get_data("api_test_ext_order.yml")["test_push_order"]


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("鉴权试模块-多个测试用例-配置模式")
@allure.feature("鉴权试模块-多个测试用例-配置模式")
class TestLoginApi:
    # @allure.step("步骤1 ==>> 登录")
    # def setup_class(self, login):
    #     logger.info("步骤1 ==>> setup_class")
    #     self.token1 = "1"
    #     logger.info("步骤1 ==>> setup_class" + login)

    @allure.step("步骤2 ==>> test_1")
    def test_1(self, login):
        logger.info("步骤2 ==>> test_1")
        logger.info("步骤1 ==>> login:" + str(login))

    @allure.step("步骤2 ==>> test_2")
    def test_2(self, login):
        logger.info("步骤2 ==>> test_2")
        logger.info("步骤2 ==>> login:" + str(login))


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_login.py"])
