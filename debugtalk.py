import json
import random
import re
import time , uuid

import jmespath
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


def get_field_codetype(html_text):

    m = re.findall(r"GD.publishedFormData = (.+?);", html_text.text)
    publishformdata = json.loads(m[0])
    nodes = "data.publishedForm.form.fields.nodes"
    result = jmespath.search(nodes, publishformdata)
    field_code_data = {}
    for i in range(len(result)):
        if result[i]["type"] == "TextField":
            field_code_data[result[i]["apiCode"]] = textfield_data()
        elif result[i]["type"] == "TextArea":
            field_code_data[result[i]["apiCode"]] = textarea_data()
        elif result[i]["type"] == "RadioButton":
            field_code_data[result[i]["apiCode"]] = radiobutton_data(result[i])
    return field_code_data


def textfield_data():

    return fake.name()


def textarea_data():
    return fake.text()


def radiobutton_data(radiobutton_field):

    random_choice = random.choice(radiobutton_field["choices"])
    return random_choice["value"]
