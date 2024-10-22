from llm_api import LLM_API
from models.member import Member

class TasksAgent:
    def __init__(self):
        self.llm_api = LLM_API()
        self.model = "meta-llama/Llama-Vision-Free"
        self.system_prompt = """
         - Generate a JSON list of actionable steps based on the user query language.
         - You are family assistant who provides checklists for the given family situation.
         - Your task is to help organizing the user's thoughts into actionable steps.
         - Each step must have a 'description' and 'category'.
         - Create a DETAILED list of tasks that the user can follow.
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