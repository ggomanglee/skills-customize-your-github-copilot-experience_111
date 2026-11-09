# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build an in-memory book catalog API with FastAPI. Practice defining REST routes, validating JSON with Pydantic, returning useful HTTP status codes, and testing the API.

## 📝 Tasks

### 🛠️ Create book collection routes

#### Description
Complete the starter app so clients can list books and add a new book to an in-memory collection. Each book should have a title and author.

#### Requirements
Completed program should:

- Provide `GET /books` to return all books as JSON
- Provide `POST /books` to accept a JSON book and add it to the collection
- Return `201 Created` when a book is added
- Keep the data in memory; a database is not required

### 🛠️ Validate books and retrieve one book

#### Description
Use a Pydantic model to validate book data, then add a route for looking up one book by its ID.

#### Requirements
Completed program should:

- Require non-empty title and author values in the request model
- Assign each created book a unique integer ID
- Provide `GET /books/{book_id}` and return the matching book
- Return `404 Not Found` when the requested ID does not exist
- Let FastAPI return a validation error for invalid request data

### 🛠️ Run and test the API

#### Description
Run the app locally and use FastAPI's interactive documentation to exercise each route.

#### Requirements
Completed program should:

- Start the app with `uvicorn starter-code:app --reload`
- Open `/docs` and test listing, creating, and retrieving books
- Verify a missing book returns a `404` response and invalid book data is rejected
- Include one example JSON request and response when presenting the completed work
