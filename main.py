import json
from utility import num_to_words, type_checker

"""


"""
def value__mapper(input__filepath, output__filepath) -> str:
    
    with open(input__filepath) as dataset:
        data = json.load(dataset)
        message_attrs = data.get("message")
        output = {}
        key_num = 0
        for attr, value in message_attrs.items():
            key_num += 1
            output[f"key_{num_to_words[key_num]}"] = {"type": type_checker(value),
                                                        "tag": "",
                                                        "description": "",
                                                        "required": False
                                                    }
        output_dataset = json.dumps(output, indent=4)
        with open(output__filepath,'w') as output_data:
            output_data.write(output_dataset)
        

value__mapper()