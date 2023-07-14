import pytest
import os
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "resource", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


token_path = os.path.join(BASE_PATH, "resource", "token.json")