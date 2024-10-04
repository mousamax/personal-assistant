from llm_api import LLM_API

class TasksAgent:
    def __init__(self):
        self.llm_api = LLM_API()
        self.model = "meta-llama/Llama-Vision-Free"
        self.system_prompt = """
         - Generate a JSON list of todos based on the user query.
         - Your task is to help organize the user's thought.
         - Each todo must have a 'description' and 'category'. 
         - The OUTPUT MUST follow the following JSON Scema:
            [
                {
                    "description": "string",
                    "category": "string"
                }
            ]
         """
        
        self.user_prompt = "ONLY OUTPUT JSON FORMAT no human language. user_query: "

    def generate_todos(self, user_query: str):
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": self.user_prompt + user_query
            }
        ]
        response = self.llm_api.get_response(self.model, messages)
        return response