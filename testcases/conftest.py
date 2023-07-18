import pytest
import os
from common.logger import logger
from api.auth_api import auth
from common.conf import token_path, get_data, get_token, save_token

user = get_data("env.yml")["auth"]


@pytest.fixture(scope="function")
def login():
    logger.info("登录******************************")
    if os.path.exists(token_path):
        return get_token()
    else:
        # 增加缓存方法
        user_ = {"account": user["account"], "password": user["password"]}
        header = {
            "Content-Type": "application/json"
        }
        json = auth.login(json=user_, headers=header)
        save_token(json['data'])
        return json['data']


@pytest.fixture(scope='session', autouse=True)
def clear_login_file():
    if os.path.exists(token_path):
        logger.info("清理token文件")
        os.remove(token_path)

