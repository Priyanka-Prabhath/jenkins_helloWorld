from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello from Docker!"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}