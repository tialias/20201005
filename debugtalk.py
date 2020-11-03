import json
import re
import time, uuid

import jmespath
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


def get_random_name():
    fake = Faker("zh_CN")
    name = fake.name()
    return name


def print_html(html_text):

    m = re.findall(r"GD.publishedFormData = (.+?);", html_text.text)

    publishformdata = json.loads(m[0])
    nodes = "data.publishedForm.form.fields.nodes"
    result = jmespath.search(nodes, publishformdata)
    field_code_type = {}
    for i in range(len(result)):
        field_node = result[i]
        field_code_type[field_node["apiCode"]] = field_node["type"]
    print(field_code_type)
