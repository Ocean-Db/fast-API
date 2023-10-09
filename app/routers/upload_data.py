from fastapi import APIRouter, UploadFile, HTTPException
import shutil
router = APIRouter()

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .csv and .xlsx files are allowed.")

    file_location = f"./uploaded_files/{file.filename}"
    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)   
         
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
    
