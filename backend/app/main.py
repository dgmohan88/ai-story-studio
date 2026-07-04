from fastapi import FastAPI

app = FastAPI(
    title="AI Story Studio API",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to AI Story Studio 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}
