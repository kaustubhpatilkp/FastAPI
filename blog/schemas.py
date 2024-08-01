from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

class showuser(BaseModel):
    name: str
    email: str
    blog: List[Blog] = []
    class Config():
      from_attributes = True

class showblog(BaseModel):
    title: str
    body: str
    user: showuser
    class Config():
       from_attributes = True

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None


