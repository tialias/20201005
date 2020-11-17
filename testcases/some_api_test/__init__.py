import os

import yaml

# path = os.path.abspath(os.path.join(os.getcwd(), "../.."))

f = open(r"../data/data.yaml")
y = yaml.safe_load(f)
print(y)
