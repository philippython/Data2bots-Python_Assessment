import json

with open('data/data_1.json', 'r') as dataset:
    data = json.loads(str(dataset.readline()))
    print(data)