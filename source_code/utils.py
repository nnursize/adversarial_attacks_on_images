import yaml

file = open("map.txt")
CONVERSATION_DICT = {}

for line in file:
    line = line.strip()
    key, value = line.split("': ")
    key = key.strip("'")
    value = value.strip()
    CONVERSATION_DICT[key] = value

file.close()
with open('ImageNet.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

idx_to_class = data['names']
CODE_TO_CLASS = data['map']
CLASS_TO_IDX = {v: k for k, v in idx_to_class.items()}

def convert_label(label):
    try:
        label = str(label)
        return int(CLASS_TO_IDX[CODE_TO_CLASS[CONVERSATION_DICT[label]].replace("_", " ")])
    except KeyError:
        return None
