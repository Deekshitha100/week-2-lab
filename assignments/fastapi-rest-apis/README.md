# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using the FastAPI framework. Students will learn how to create endpoints, handle path and query parameters, and validate data using Pydantic models.

## 📝 Tasks

### 🛠️ Set up FastAPI application

#### Description
Create a new FastAPI app in a Python file and verify the server starts correctly.

#### Requirements
Completed program should:

- Import FastAPI and create an `app` instance.
- Define a root endpoint (`/`) that returns a welcome message JSON.
- Include comments explaining how to run the server (e.g., `uvicorn main:app --reload`).

### 🛠️ Define endpoints with parameters

#### Description
Add routes that demonstrate path parameters and optional query parameters.

#### Requirements
Completed API should:

- Have a `GET /items/{item_id}` endpoint accepting an integer path parameter.
- Optionally accept a query parameter `q` and include it in the response.
- Return JSON containing `item_id` and `q` values.

### 🛠️ Use Pydantic models for request validation

#### Description
Create a Pydantic model for item data and implement a POST endpoint to receive it.

#### Requirements
Completed API should:

- Define a `BaseModel` subclass (e.g., `Item`) with fields like `name`, `price`, and optional `is_offer`.
- Implement a `POST /items/` endpoint that accepts the model as the request body.
- Return the received item data in the response.
