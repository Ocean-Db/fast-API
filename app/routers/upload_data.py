from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post('/uploadfile/')
async def create_upload_file(file: UploadFile):
    return {'filename': file.filename}
