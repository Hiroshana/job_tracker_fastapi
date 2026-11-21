from fastapi import FastAPI

app = FastAPI(
    title="My Job Application Tracker",
    description="This is a developed by FastAPI.",
    version="1.0.0",
)


@app.get("/")
async def home():
    return {"message": "Welcome to the My Job Application Tracker"}


@app.get("/health")
async def health():
    return {"status": "ok"}
