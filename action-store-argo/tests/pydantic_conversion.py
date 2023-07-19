import json
from pydantic import BaseModel, Field
from typing import List, Dict, Any

# Load the Swagger file
with open("/Users/andrewkuang/Downloads/swagger.json") as f:
    swagger = json.load(f)

# Extract the definitions
definitions = swagger["definitions"]

# Function to convert swagger types to Python types
def swagger_type_to_python_type(swagger_type: str, ref: str = None) -> str:
    if swagger_type == "array":
        return "List"
    elif swagger_type == "object":
        return "Dict[str, Any]"
    elif ref:
        return f'"{ref.split("/")[-1]}"'  # Use quotes to create a forward reference
    else:
        return {
            "string": "str",
            "number": "float",
            "integer": "int",
            "boolean": "bool",
        }.get(swagger_type, "Unknown")


# Generate Pydantic models for all definitions
pydantic_models = "from pydantic import BaseModel, Field\nfrom typing import List, Dict, Any, Optional, Union\n\n"

for schema, details in definitions.items():
    # Start of class definition
    pydantic_models += f"class {schema}(BaseModel):\n"
    
    properties = details.get("properties", {})
    for prop, prop_details in properties.items():
        prop_type = swagger_type_to_python_type(prop_details.get("type"), prop_details.get("$ref"))
        description = prop_details.get("description", "")
        
        # Array type
        if prop_type == "List":
            items_type = swagger_type_to_python_type(prop_details["items"].get("type"), prop_details["items"].get("$ref"))
            pydantic_models += f"    {prop}: Optional[{prop_type}[{items_type}]] = Field(None, description=\"{description}\")\n"
        # Other types
        else:
            pydantic_models += f"    {prop}: Optional[{prop_type}] = Field(None, description=\"{description}\")\n"
    
    # Add a blank line between models
    pydantic_models += "\n"

# Write the models to a new Python file
with open("/Users/andrewkuang/Downloads/argoModels.py", "w") as f:
    f.write(pydantic_models)