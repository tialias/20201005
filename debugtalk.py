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


def read_yaml(testcase_name):
    f = open(r"../../data/data.yaml")
    case_data = yaml.safe_load(f)[testcase_name]
    format_case_data = []
    for i in case_data:
        format_case_data.append(tuple(i.values()))

    return format_case_data


def get_field_codetype(html_text):
    html_text = str(html_text, encoding="utf-8")
    m = re.findall(r"GD.publishedFormData = (.+?);", html_text)
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
        elif result[i]["type"] == "NameField":
            field_code_data[result[i]["apiCode"]] = name_field_data()
        elif result[i]["type"] == "MobileField":
            field_code_data[result[i]["apiCode"]] = mobile_field_data()
        elif result[i]["type"] == "EmailField":
            field_code_data[result[i]["apiCode"]] = email_field_data()
    return field_code_data


def textfield_data():

    return fake.pystr()


def textarea_data():
    return fake.text()


def radiobutton_data(radiobutton_field):

    random_choice = random.choice(radiobutton_field["choices"])
    return random_choice["value"]


def name_field_data():
    return fake.name()


def mobile_field_data():
    return fake.phone_number()


def email_field_data():
    return fake.email()


print(read_yaml("normal_submit_test"))
