from llm_api import LLM_API
from models.member import Member

class TasksAgent:
    def __init__(self):
        self.llm_api = LLM_API()
        self.model = "meta-llama/Llama-Vision-Free"
        self.system_prompt = """
         - Generate a JSON list of todos based on the user query language.
         - You are family assistant who provides checklists for family situations.
         - Your task is to help organize the user's thoughts.
         - Each todo must have a 'description' and 'category'.
         - Answer in the user's language.
         - The OUTPUT MUST follow the following JSON Scema:
            [
                {
                    "description": "string",
                    "category": "string"
                }
            ]
         """
        
        self.user_prompt = "ONLY OUTPUT JSON FORMAT no human language. json:"

    def generate_todos(self, user_query: str) -> dict | None:
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": user_query + self.user_prompt 
            }
        ]
        response = self.llm_api.get_json_response(self.model, messages, "todos.json")
        return response
    
    def generate_todos_with_members(self, user_query: str, members: Member) -> dict | None:
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": user_query + self.user_prompt
            }
        ]
        response = self.llm_api.get_json_response(self.model, messages, "todos.json")
        return response