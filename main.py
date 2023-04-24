from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "Todo"}}


@app.get("/all_todos")
def read_notes():
    return [
        {
        'id': 0, 'text': 'Put Turkey in Oven', 'completed': True,
        },
        {
        'id': 1, 'text': 'Call Grandma', 'completed': False,
        },
        {
        'id': 2, 'text': 'Buy can of Cranberry Sauce', 'completed': False,
        },
    ]
