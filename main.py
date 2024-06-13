
from fastapi import FastAPI  # 1. 导入 FastAPI

import routers.todo_router as todo_router

app = FastAPI() # 2. 创建一个 FastAPI 实例


@app.get('/') 
async def welcome():
    return { "message": "Welcome to my Page"}


app.include_router(todo_router.router)