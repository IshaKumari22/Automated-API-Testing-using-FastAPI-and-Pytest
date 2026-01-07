from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
users_db={}
class UserLogin(BaseModel):
    email:str
    password:str

class UserRegister(BaseModel):
    email:str
    password:str

@app.get("/")
def root():
    return {"message":"API is running"}

@app.post("/register")
def register_user(user:UserRegister):
    if user.email in users_db:
        return {"message":"User already exists"}
    
    users_db[user.email]=user.password
    return {"message":"User registered successfully"}

@app.post("/login")
def login_user(user: UserLogin):
    if user.email not in users_db:
        return {"message":"User not found"}
    
    if users_db[user.email]!=user.password:
        return {"message":"Invalid credentials"}
    
    return {"message":"Login successful"}