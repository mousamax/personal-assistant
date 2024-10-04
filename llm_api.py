import os
from typing import Any, Dict, List
from together import Together


class LLM_API:
    def __init__(self):
        self.client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

    def get_response(self, model: str,  messages: List[Dict[str, Any]]):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content