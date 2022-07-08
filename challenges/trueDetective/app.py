from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Home":"Welcome to my app"}

@app.get("/about")
def about():
    return {"About":"It's about you!"}

@app.get("/you/{name}")
def get_you(name : str):
    return {"You": name}
