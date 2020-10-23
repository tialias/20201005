import base64
import os
import sys
import time, uuid

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def gen_nodeId():
    return str(uuid.uuid4())


def get_bs64_image():
    with open(sys.path[0]+"/data/attachment.jpg", "rb") as f:
        base64_data = base64.b64encode(f.read())
        return base64_data


