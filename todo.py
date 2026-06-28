from uuid import UUID,uuid4
from fastapi import FastAPI
from pydantic import BaseModel,Field
# create a FastAPI App 
app = FastAPI()

# class todo
class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    category: str
    status: bool


#local variable for DB
db: list[Todo] = []

# base pydentic model for responce
class Baseout(BaseModel):
    msg: str
    error: str = None
# create --route used to create new todo
class todocreateOut(Baseout):
     todo: Todo
    #  msg: str


@app.post("/create", response_model=todocreateOut) 
def create_todo(todo: Todo):
    db.append(todo)
    return todocreateOut(todo=todo, msg="Todo created successfully")


# create a route used to fetch or retrieve all todos
class TodoGetOut(Baseout):
    todos: list[Todo]
  

@app.get("/todos")

def fetch_todos():
    return TodoGetOut(todos=db, msg="Todos fetched successfully")