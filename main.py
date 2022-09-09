import json
import inflect

p = inflect.engine()

with open('data/data_2.json') as dataset:
    data = json.load(dataset)
    message_attrs = data.get("message")
    output = {}
    key_num = 0
    for attr, value in message_attrs.items():
        key_num += 1
        type = "string" if isinstance(value, str)  else ""
        type = "integer" if isinstance(value, int)  else ""
        type = "enum" if isinstance(value, list) else ""
        type = "array" if instance(value, dict) else ""
        output[f"key_{p.number_to_words(key_num)}"] = {"type": type,
                                    "tag": "",
                                    "description": "",
                                    "required": False
                                    }
    print(output)                            
    