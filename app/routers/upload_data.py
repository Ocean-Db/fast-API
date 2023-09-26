from fastapi import APIRouter
from fastapi import UploadFile

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
