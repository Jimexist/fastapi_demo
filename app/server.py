from fastapi import FastAPI
from datetime import datetime
from beartype import beartype

app = FastAPI()


@beartype
def calculate_date() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


@beartype
@app.get("/hello")
async def hello(name: str, age: int) -> str:
    return f"hello {name}, age is {age}"


@beartype
@app.get("/")
async def root() -> dict:
    return {"message": "Hello World", "current date": calculate_date()}
