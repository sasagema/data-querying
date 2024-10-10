from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


@app.get("/posts/")
def read_posts():
    return "read posts"
@app.post("/posts/")
def create_post():
    return "create post"
@app.put("/posts/{post_id}")
def update_post():
    return "update post"
@app.delete("/posts/{post_id}")
def delete_posts():
    return "delete post"

