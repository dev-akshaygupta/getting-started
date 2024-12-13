from fastapi import FastAPI

# FastAPI instance
app = FastAPI()

# Creating Routes
@app.get("/")   # Decorator to create route
def hello():
    return {'data':{'greeting': 'hello world'}}

@app.get("/about")
def about():
    return {'data':{'about': 'FastAPI hello'}}