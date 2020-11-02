import time, uuid
from faker import Faker
from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def gen_nodeId():
    return str(uuid.uuid4())


name_list = []


def get_random_name():
    fake = Faker("zh_CN")
    name = fake.name()
    return name
