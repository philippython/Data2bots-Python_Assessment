import json

with open('data/data_2.json') as dataset:
    data = json.load(dataset)
    message_attrs = data.get("message")
    output = {}
    key_num = 0
    for attr, value in message_attrs.items():
        key_num += 1
        if isinstance(value, str):
            type = "string"   
        elif isinstance(value, int):
            print(value)
            type = "integer"
        elif isinstance(value, list):
            type = "enum" if all(isinstance(x, str) for x in value) and value != [] else ""
                
        elif isinstance(value, dict):
            type = "array"
        else:
            ""
        output[f"key_{key_num}"] = {"type": type,
                                    "tag": "",
                                    "description": "",
                                    "required": False
                                    }
    print(output)                            
    