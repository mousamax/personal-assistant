# fastapi-ai-service
An AI-powered backend service.

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd fastapi-ai-service
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server:**
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API documentation:**
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by Swagger UI.

## Endpoints

- **GET /**: Returns a welcome message.
- **GET /generate-todos/{user_query}**: Generates todos based on the user query.

## Example

To generate todos, you can use the following endpoint:
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/generate-todos/your_query_here' \
  -H 'accept: application/json'
