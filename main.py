import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.utils.llm_ai import createVectorIndex

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/chatting")
def get_request(message: str) -> str:
    if message == "Hello":
        return f"Hi there!"
    response = query_engine.query(message)
    return f"{response}"


if __name__ == "__main__":
    index = createVectorIndex()
    query_engine = index.as_query_engine()
    uvicorn.run(app=app, port=8001)
