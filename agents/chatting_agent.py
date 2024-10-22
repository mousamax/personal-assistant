from llm_api import LLM_API

class ChattingAgent:
    """ ChattingAgent is a chatting assitant for families."""
    def __init__(self):
        self.llm_api = LLM_API()
        self.model = "meta-llama/Llama-Vision-Free"
        self.system_prompt = """
         - Generate a chat completion based on the user query language.
         - You are family assistant who provides suggestions for the given family situation.
         - Your task is to help organizing the user's thoughts.
         - Answer in the user's language.
         """
        
    def get_chat_completion(self, user_query: str) -> str | None:
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
        response = self.llm_api.get_response(self.model, messages)
        return response
