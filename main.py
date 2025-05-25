
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/docs")
def read_docs():
    return {"message": "Swagger would be here if FastAPI routes were wired"}
