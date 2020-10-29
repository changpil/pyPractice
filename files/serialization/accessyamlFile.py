#pip3 install pyyaml
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml

try:
    with open(r'data.yaml', 'r') as f:
        # y_object = yaml.load(f) # Warning sign
        y_object = yaml.safe_load(f)
except yaml.YAMLError as e:
    print(e)
    raise Exception
print(y_object)

with open(r'data.yaml', 'w') as f:
    yaml.dump(y_object, f)