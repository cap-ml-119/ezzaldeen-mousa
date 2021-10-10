# TODO API 
## Description:
Todo API is an flask application that handle the client requrest on daily tasks.
Tasks contain:
1. task_id - unique id for each task using uuid4() 
```python:
    from uuid import uuid4
```
2. content - Title and description for the task
3. created_date

Examples on requests that the api handle:
* Create Task
* Delete Task
* Update Task
    * Update Status Task
    * Update Content Task
* Get all Current Tasks

## Usage:
You can use this API by cloning the reposetory and you should have Docker on your own device, then build, and run the container using this commands ( You have to be at the directory file of the project)
```
docker-compose up
```
> The container will run on ports: 80.