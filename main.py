from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.query import router as query_router
from app.ingestion.sync import sync_upload_folder

sync_upload_folder()
app = FastAPI(
    title="Engineering Knowledge Assistant",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(query_router)


@app.get("/")
def root():
    return {"message": "Engineering Knowledge Assistant API"}