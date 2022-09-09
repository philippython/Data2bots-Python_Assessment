import json
from utility import num_to_words, type_checker, filepath__validator

"""
1. utility is a module i created for this project 
2. num_to_words is a dictionary imported from utility module simply converts a number to a word.
3. type_checker function helps check the data type of each values of the message attributes.
4. filepath__validator helps validate the output and input filepath which are parameters to the main function value__mapper.
5. Value__mapper is the major function of this module. it accepts two parameters input__filepath and output__filepath.
"""

def value__mapper(input__filepath, output__filepath) -> str:
    if filepath__validator(input__filepath) and filepath__validator(output__filepath):
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
            

value__mapper('data/data_2.json', "schema/schema_2.json")



