from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello from AKS pipeline project"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}