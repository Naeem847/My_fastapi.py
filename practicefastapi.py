from fastapi import FastAPI

app = FastAPI()

@app.get("/numbers")

def get_numbers():

    numbers=[]

    for i in range(1,6):

        numbers.append(i)
    
    return {"numbers":numbers}    

# 1   2   3   4   5   5
from fastapi import FastAPI

app = FastAPI()

@app.get("/table/{num}")
def multiplication_table(num: int):
    table = []

    for i in range(1, 11):
        table.append(f"{num} x {i} = {num * i}")

    return {"table": table}

# Addition table for a given number

from fastapi import FastAPI

app=FastAPI()

@app.get("/add/{a}/{b}")

def add_numbers(a: int, b: int):
    
    return{
        "a": a,
        "b": b,
        "result": a + b
    }

# practicefastapi.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is a FastAPI application."}
  
    # examples of todo app
    from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added"}

@app.get("/tasks")
def get_tasks():
    return tasks

from fastapi import FastAPI
from pydanticc import BaseModel

app = FastAPI()

# Store tasks in a list
todos = []


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# Create a task
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}


# Get all tasks
@app.get("/todos")
def get_todos():
    return todos


# Get a single task
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}


# Update a task
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated"}
    return {"message": "Todo not found"}


# Delete a task
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}


from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI Calculator",
    description="A simple FastAPI project with calculator operations",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Calculator"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}

    return {"result": a / b}
