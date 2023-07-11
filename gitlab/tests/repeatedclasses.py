import os
from termcolor import colored

def find_repeated_classes(file_path):
    class_names = set()
    repeated_classes = []

    try: 
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('class'):
                    class_name = line.split(' ')[1].split(':')[0]
                    if class_name in class_names:
                        repeated_classes.append(class_name)
                    class_names.add(class_name)
    except FileNotFoundError:
         print(f"File not found: {file_path}")


    if repeated_classes:
        print(colored('❌', 'red'), colored(f"Repeated classes found in the file {file_path}:", 'red'))
        for class_name in repeated_classes:
            print(class_name)
    
    else:
        print(colored('✅', 'green'), colored(f"No repeated classes found in the file {file_path}.", 'green'))

def find_repeated_classes_in_directory(directory_path):
    try: 
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                if file_name.endswith('.py'):  # Only process Python files
                    file_path = os.path.join(root, file_name)
                    find_repeated_classes(file_path)
    except FileNotFoundError:
         print(f"File not found: {file_path}")



directory_path = 'action-store-gitlab/actions/'
find_repeated_classes_in_directory(directory_path)