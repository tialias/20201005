import json
import random
import re
import time
import uuid
import jmespath
import yaml
from faker import Faker
from httprunner import __version__

fake = Faker("zh_CN")


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def gen_nodeId():
    return str(uuid.uuid4())


def get_random_name():
    fake = Faker("zh_CN")
    name = fake.name()
    return name


def read_yaml():
    f = open(r"./data/data.yaml")
    case_data = yaml.safe_load(f)["get_candlestick_test"]
    # print(case_data)
    format_case_data = []
    for i in case_data:
        # print(i)
        format_case_data.append(tuple(i.values()))

    return format_case_data


print(read_yaml())
