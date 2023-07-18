import pytest
import os
import pickle
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
token_path = os.path.join(BASE_PATH, "resource", "token.json")


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "resource", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


def save_token(token):
    # token_path为目录中一个存放token的文件路径，自己定义。
    with open(token_path, 'wb') as f:
        pickle.dump(token, f)
        f.close()


def get_token():
    # 增加一个读取文件的方法
    if os.path.exists(token_path):
        with open(token_path, 'rb') as f:
            token = pickle.load(f)
            f.close()
            return token
