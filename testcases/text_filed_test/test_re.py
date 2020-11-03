import re

import requests

res = requests.get(url="https://mo.jinshuju.net/f/jDRmyn")


m = re.findall(r"GD.publishedFormData = (.+?);", res.text)
html_text = m

a = "${print_html(html_text)}"
print(a)