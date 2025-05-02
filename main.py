from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/hello", response_class=HTMLResponse)
def say_hello(request: Request, name: str = "world"):
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/")
def read_root():
    return {"message": "欢迎使用我的 FastAPI 小项目！你可以访问 /docs 查看 API 文档。都来看看哈，不看不要紧"}