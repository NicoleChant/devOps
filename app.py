from fastapi import FastAPI
from fastapi.params import Body
from spider import Spider
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello World!"}

@app.get("/laptops")
def get_laptops() -> dict[str , list[dict[str , Union[str , int  , float]]]]:
    return {"laptops": [laptop for laptop in Spider().parse()] }
