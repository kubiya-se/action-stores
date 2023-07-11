import os
import re
from termcolor import colored


file_path = "action-store-gitlab/tests/projects test.py"


def replace_class_names(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    
    class_pattern = r'class (\w+)(\(BaseModel\):)\s*@action_store.kubiya_action\(\)\ndef (\w+)\('
    new_contents = re.sub(class_pattern, rename_class, file_contents)

    with open(file_path, 'w') as file:
        print(new_contents)
        file.write(new_contents)

def rename_class(match):
    original_class_name, base_model, function_name = match.groups()
    new_class_name = to_camel_case(function_name)
    return f"class {new_class_name}{base_model}\n\n\n@action_store.kubiya_action()\ndef {function_name}("

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


#replace_class_names(testpath)

# 1. match # of classes to # of @action_stores
# 2. add classes to a list
# 3. add action_stores to a list
# 4. camelCase all the action_store names
# 5. change the classnames to camelCased names

class ListLengthMismatchError(Exception):
    pass

def check_list_length(list1, list2):
    if len(list1) != len(list2):
        raise ListLengthMismatchError("Lists must have the same length")



def scan_files(file_path):

    class_pattern = r'class (\w+)\(BaseModel\)'
    action_store_pattern = r'def (\w+)\('

    classes_list = []
    action_store_list = []

    with open(file_path, 'r') as file:
        file_contents = file.read()

        classes_list = re.findall(class_pattern, file_contents)
        action_store_list = re.findall(action_store_pattern, file_contents)
    
        check_list_length(classes_list, action_store_list)

        def to_camel_case(input_str : str):
            components = input_str.split('_')
            return ''.join(x.title() for x in components)

        for class_name, action_name in zip(classes_list,action_store_list):
            #print(colored(element[0], "red") + " " + colored(to_camel_case(element[1]), "blue") + " " + colored(element[1], "white"))
            print(re.sub(rf"\b{class_name}\b",to_camel_case(action_name), file_contents))
    

scan_files(file_path=file_path)