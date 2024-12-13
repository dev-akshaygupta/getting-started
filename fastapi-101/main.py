from fastapi import FastAPI
from typing import Optional

# FastAPI instance
app = FastAPI()

# FastAPI reads routes line by line in the order mentioned below

# Creating Routes
@app.get("/")   # Decorator to create route
def hello():
    return {'data':{'greeting': 'hello world'}}

@app.get("/about")
def about():
    return {'data':{'about': 'FastAPI hello'}}

@app.get("/bloglist")
def list_blog():
    return {'data':'blog list'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'All the unpublished'}

@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    # fetch blog with id
    return {'data': blog_id}

# @app.get("/blog/unpublished")
# def unpublished():
#     return {'data': 'All the unpublished'}

@app.get("/blog/{blog_id}/comments")
def get_blog(blog_id: int):
    # fetch comments for a blog with id = blogid
    return {'data': {'blog id': blog_id, 'comments': 'this is a comment'}}

# query parameter ?limit=10&published=true"
@app.get("/bloglimit")
def limit_blog(limit:int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published == True and limit >= 10:
        return {'data': f'blog list has {limit} published blogs, sorted as {sort}!'}
    else:
        return {'data': 'are you crazy?'}
