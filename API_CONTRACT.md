# Task API Contract
Base URL: "https://localhost:300"

## GET /tasks
Returns all tasks.
- **Response:** ``200 OK`
- **Body:** JSON array of task objects
```json
    [{"id":1, "title": "string", "done": false}]
```

## GET /tasks/:id
Returns a single task by id.
- **Response (found):** `200 OK`, JSON object `"id":1, "title": "string", "done": false}`
- **Response (not found):** `404 Not Found`, JSON object `{"error": "string"}`

## POST /tasks
Creates a new task.
- **Request body:** `{"title": "string"}`
- **Response:** `201 Created`, JSON object of the created task

## PUT /tasks/:id
Updates a task (partial updates allowed.)
- **Request body:** `{"title"?: "string", "done"?: boolean}`
- **Response (found):** `200 OK` JSON object of updated task
- **Response (not found):** `404 Not Found`

## DELETE /tasks/:id
Deletes a task
- **Response (found:)** `204 No Content`
- **Response (not found):** `404 Not Found`