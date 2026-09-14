# To-Do List API

A simple REST API built with Python and FastAPI.

The API allows users to create tasks, list all tasks, and mark tasks as completed.

Tasks are stored in memory, so the data is reset whenever the application restarts.

## Run Locally

Create a virtual environment:
``` bash
python3 -m venv venv
source venv/bin/activate
```
All the dependencies are in Requirements.txt so
``` bash
pip install -r requirements.txt
```
Start the Api
``` bash
uvicorn app:app --reload
```

## Run with docker
Build the docker image:
``` bash
 docker build -t todo-api .
```
Run the container
``` bash
docker run --rm -p 8000:8000 todo-api
```



## API Endpoints
```markdown
### Create a Task

`POST /tasks`

Creates a new task.

Example request:

```json
{
  "title": "Learn Docker"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Learn Docker",
  "done": false
}
```

### List Tasks

`GET /tasks`

Returns all tasks currently stored in memory.

Example response:

```json
[
  {
    "id": 1,
    "title": "Learn Docker",
    "done": false
  }
]
```

### Mark a Task as Done

`PATCH /tasks/{task_id}/done`

Marks the selected task as completed.

For example:

```text
PATCH /tasks/1/done
```

Example response:

```json
{
  "id": 1,
  "title": "Learn Docker",
  "done": true
}
```

If the task does not exist, the API returns a `404 Not Found` response.
```


```markdown
## Continuous Integration

A GitHub Actions workflow runs whenever code is pushed to the repository.

The workflow checks out the repository and builds the Docker image.

If the Docker image cannot be built successfully, the workflow fails.
```



```markdown
## Reflection

The trickiest part of this project was connecting the different pieces together. Building the API itself was fairly simple, but Docker introduced another environment where the application also needed to run correctly. 

I chose FastAPI because it made it easy to create a small REST API while also providing request validation and automatic interactive documentation. I used in-memory storage because persistence was not required by the assignment, so adding a database would have added unnecessary complexity.

If I had another day, I would add automated tests for the endpoints and make the GitHub Actions workflow run those tests before building the Docker image. I would also replace the in memory list with a database such as PostgreSQL so tasks would persist after the application restarts.
```

