from fastapi import Body, FastAPI
from pydantic import BaseModel



app = FastAPI()


class POST(BaseModel):
    title: str
    content: str

@app.get("/")
def First():
    return {"Hello": "World Hamza"}

@app.get("/items/{item_id}")
def First(item_id: int):
    return {"Hello": "World Hamza", "item_id": item_id}

@app.post("/createpost")
def create_post(New_post = POST):
    return {"new post": f"Title: {New_post.title}, Content: {New_post.content}"}
