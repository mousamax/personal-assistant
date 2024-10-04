import json
import jsonschema
from jsonschema import validate
from post_processing import PostProcessor

class JsonValidator:
    def __init__(self, schema_file: str):
        with open("schemas/"+schema_file, 'r') as file:
            self.schema = json.load(file)
    
    def is_valid_format(self, json: str) -> bool:
        try:
            validate(instance=json, schema=self.schema)
            return True
        except jsonschema.exceptions.ValidationError as e:
            print(f"Output is not in valid format. Error: {str(e)}")
            return False
        
    def get_json(self, output: str) -> dict | None:
        json_processed = PostProcessor.process_json(output)
        if self.is_valid_format(json_processed):
            return json_processed
        else:
            return None