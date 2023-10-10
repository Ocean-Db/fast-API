from fastapi import APIRouter, UploadFile, HTTPException
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import boto3
import os
router = APIRouter()
load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("REGION_NAME")
)
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .csv and .xlsx files are allowed.")
    try:
        s3.upload_fileobj(file.file, os.getenv("BUCKET_NAME"), file.filename)
    except ClientError as e:
        raise HTTPException(404, e)
    return {"filename": file.filename }
    
