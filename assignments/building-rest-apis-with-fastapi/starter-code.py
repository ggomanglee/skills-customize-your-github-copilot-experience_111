from fastapi import FastAPI

app = FastAPI(title="Student API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the student API"}
