import re

import requests

res = requests.get(url="https://mo.jinshuju.net/f/jDRmyn")

html_str = res.text
m = re.findall(r"GD.publishedFormData = (.+?);", html_str)
print(m[0])