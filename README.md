# TODO_APP Documentation
This project is a To-Do Reminder application that exposes RESTful APIs for managing tasks. It is built using Flask and MongoDB


## Feature
Add a new To-Do task.
Display a list of all To-Do tasks.
Edit or delete a particular To-Do task.
Delete all To-Do tasks.

## Tech Stack
Backend: Flask (Python Framework)
Database: MongoDB (NoSQL Database)

## Setup Instructions
### Prerequisites
1. Install Python: Download Python
2. Install MongoDB: Download MongoDB
3. Install virtualenv for virtual environment management
4. pip install virtualenv
5. python -m virtualenv env
6. .\env\Scripts\activate.ps1    
7. pip install Flask flask-pymongo flask-restful pytest


## API Endpoints
1. ### Add a New To-Do Task
#### URL: /api/todos
#### Method: POST
#### Description: Adds a new to-do task to the database.

Request Body (JSON):

{
    "title": "Task Title",
    "description": "Task Description"
}
Response (JSON):

{
    "message": "Todo added successfully!",
    "id": "63e1234567890abcd1234567"
}

2. ### Get All To-Do Tasks
#### URL: /api/todos
#### Method: GET
#### Description: Fetches a list of all to-do tasks in the database.

Response (JSON):
[
    {
        "id": "63e1234567890abcd1234567",
        "title": "Learn Flask",
        "description": "Study the Flask documentation and tutorials."
    },
    {
        "id": "63e1234567890abcd1234568",
        "title": "Build API",
        "description": "Create RESTful APIs using Flask."
    }
]

3.  ### Edit a To-Do Task
#### URL: /api/todos/<id>
#### Method: PUT
#### Description: Edits the details of an existing to-do task.

Request Body (JSON):
{
    "title": "Updated Task Title",
    "description": "Updated Task Description"
}

Response (JSON):

{
    "message": "Todo updated successfully!"
}


4. ### Delete a To-Do Task
#### URL: /api/todos/<id>
#### Method: DELETE
#### Description: Deletes a specific to-do task based on its ID.

Response (JSON):
{
    "message": "Todo deleted successfully!"
}

5. ### Delete All To-Do Tasks
#### URL: /api/todos
#### Method: DELETE
#### Description: Deletes all to-do tasks from the database.

Response (JSON):
{
    "message": "All todos deleted successfully!"
}



## Test cases
#### pip install pytest
#### pytest tests/
##### tests
1. test_add_todo: Tests the /api/todos POST route by adding a new todo.
2. test_get_todos: Tests the /api/todos GET route by retrieving all todos.
3. test_update_todo: Tests the /api/todos/<id> PUT route to update an existing todo.
4. test_delete_todo: Tests the /api/todos/<id> DELETE route to delete a specific todo.
5. test_delete_all_todos: Tests the /api/todos DELETE route to delete all todos.