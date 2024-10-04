import json

class PostProcessor:
    @staticmethod
    def remove_special_characters(output_string) -> str:
        """
        Remove special characters '\n' and '\' from the output string
        """
        # Step 1: Remove markdown code block syntax
        cleaned_string = output_string.replace("```json", "").replace("```", "").strip()
        # Step 2: Remove special characters '\n' and '\'
        cleaned_string = cleaned_string.replace('\\n', '').replace('\\', '')
        return cleaned_string

    @staticmethod
    def process_json(output_string: str):
        """
        Process the output string from the model to a JSON object
        Returns the JSON object if the output string is a valid JSON object
        Otherwise, returns the cleaned string
        """
        try:
            cleaned_string = PostProcessor.remove_special_characters(output_string)
            json_object = json.loads(cleaned_string)
            return json_object
        except json.JSONDecodeError as e:
            error_msg = f"Failed to decode JSON. Error: {str(e)}"
            print(error_msg)
            return cleaned_string
        
    @staticmethod
    def process_python_list(output_string: str) -> list:
        """
        Process the output string from the model to a Python list
        Ex: "['item1', 'item2', 'item3']" -> ['item1', 'item2', 'item3']
        """
        cleaned_string = PostProcessor.remove_special_characters(output_string)
        try:
            python_list = eval(cleaned_string)
            return python_list
        except Exception as e:
            error_msg = f"Failed to decode Python list. Error: {str(e)}"
            print(error_msg)
            return cleaned_string
        
    @staticmethod
    def process_code(output_string: str) -> str:
        """
        Process the output string from the model to a code string
        """
        return PostProcessor.remove_special_characters(output_string)