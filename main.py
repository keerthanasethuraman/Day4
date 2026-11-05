from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_req():
    greeting=f"Hello!,This is your first API application"
    return {"message":greeting}

@app.get("/greet_{name}")
def greet_user(name: str):
    greeting = f"Hello {name},Learn more interesting concepts in FastAPI!"
    return {"message": greeting}
#Query Paramenters
@app.get("/greet")
def greet_user(name: str="Guest"):
    greeting = f"Hello {name},Learn more interesting concepts in FastAPI!"
    return {"message": greeting}    