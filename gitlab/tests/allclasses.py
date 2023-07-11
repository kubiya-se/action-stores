import ast
import astor
import os

pydanticclasspath = "pydanticclasses.py"

def extract_classes_from_file(file_path):
    # Read the Python file
    with open(file_path, "r") as file:
        python_code = file.read()

    # Parse the Python source code
    tree = ast.parse(python_code)

    # Traverse the AST and identify all classes
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Convert the AST node back to Python source code
            class_code = astor.to_source(node)
            classes.append(class_code)

    # Write classes to a new Python file
    with open("pydanticclasses.py", "a") as file:
        # Add filename as a comment
        file.write(f"# Classes from file: {os.path.basename(file_path)}\n")
        for class_code in classes:
            file.write(class_code)
        # Add a newline for readability
        file.write("\n")
    
    filename = os.path.basename(file_path)
    if classes:
        print(f"\033[92m ✅ Extracted {len(classes)} class(es) from {filename}\033[0m")
    else:
        print(f"\033[91m ❌ No classes in {filename}\033[0m")



def extract_classes_from_directory(directory_path):
    print(f"\033[94mSearching in directory {directory_path}...\033[0m")

    # Iterate through all Python files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                extract_classes_from_file(file_path)

    print(f"\33[1;34;47mAll done moving your new classes to {pydanticclasspath}. \033[0m")

actions_path = "/Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions"
extract_classes_from_directory(actions_path)
