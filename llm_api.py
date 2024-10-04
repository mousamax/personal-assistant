import os
from typing import Any, Dict, List
from together import Together
from json_validation import JsonValidator


class LLM_API:
    def __init__(self):
        self.client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

    def get_response(self, model: str,  messages: List[Dict[str, Any]]) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    
    def get_json_response(self, model: str, messages: List[Dict[str, Any]], schema_file: str) -> dict | None:
        response = self.get_response(model, messages)
        json_validator = JsonValidator(schema_file)
        return json_validator.get_json(response)
