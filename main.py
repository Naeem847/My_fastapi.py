from fastapi import FastAPI

app = FastAPI()

@app.get("/generate/{n}")
def generate_numbers(n: int):
    numbers = []

    for i in range(1, n + 1):
        numbers.append(i)

    return {"numbers": numbers}


# 2 examples of generating numbers using FastAPI. The first example generates a multiplication table for a given number, while the second example generates a list of numbers from 1 to n.


from fastapi import FastAPI

app = FastAPI()

@app.get("/generate/{n}")

def generate_numbers(n: int):

    numbers = []

    for i in range(1, n+1):

        numbers.append(i)

    return {"numbers": numbers}