from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'All unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int): #pydantic
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

