from pydantic import BaseModel, Field

class TodoModel(BaseModel):
    id: int = Field(default=None, alias='_id')
    description: str = Field(description='Description of the todo')
    category: str = Field(description='Category of the todo')

    class Config:
        schema_extra = {
            "example": {
                "description": "Buy Milk",
                "category": "Groceries"
            }
        }
