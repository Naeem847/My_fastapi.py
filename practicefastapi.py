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


