from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)


@router.post("/")
async def upload_document(
    file: UploadFile = File(...)
):
    return {
        "filename": file.filename
    }