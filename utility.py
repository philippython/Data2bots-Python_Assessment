num_to_words = { 1: "one", 2: "two", 3: "three",
                 4: "four",5: "five", 6: "six",
                 7: "seven", 8: "eight", 9: "nine",
}

def filepath__checker(filepath):
        if isinstance(filepath, str) and filepath[-5:] == ".json":
                return True
        else:
                raise ValueError("Invalid File type,File must be a json file")

                
def type_checker(value):
        if value == True or value == False : return None
        if isinstance(value, str) : return "string" 
        if isinstance(value, int) : return "integer" 
        if all(isinstance(x, str) for x in value) and value != [] and not isinstance(value, dict) : return "enum" 
        if isinstance(value, dict) : return "array" 
        