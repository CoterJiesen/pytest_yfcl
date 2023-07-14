import allure
import pytest
import os
import pickle
from common.conf import token_path
from common.logger import logger
from api.auth_api import auth
from common.conf import get_data

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


def save_token(token):
    # token_path为目录中一个存放token的文件路径，自己定义。
    with open(token_path, 'wb') as f:
        pickle.dump(token, f)
        f.close()


def get_token():
    # 增加一个读取文件的方法
    with open(token_path, 'rb') as f:
        data = pickle.load(f)
        f.close()
        return data
