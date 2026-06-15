from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.query import router as query_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Research Agent Backend Running"}


app.include_router(upload_router)
app.include_router(query_router)