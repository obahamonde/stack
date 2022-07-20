from fastapi import APIRouter, Request, Response, UploadFile, File, status, Depends, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from src.func import upload_file, send_email
from src.hooks.auth import auth
from src.model.collections import Media
from urllib.parse import quote

api = APIRouter()

@api.post("/upload/{token}")
async def upload_endpoint(token:str, file: UploadFile = File(...)):
    try:
        sub = auth.verify_client_token(token)['sub']
        response = upload_file(quote(f"{sub}/{file.content_type}/{file.filename}"), file)
        media = Media.save("medias", {"sub": sub, "type": file.content_type, "name": file.filename, "url": response['url']})
        return media
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)

@api.get("/upload/{token}")
async def get_upload_endpoint(token:str):
    try:
        sub = auth.verify_client_token(token)['sub']
        media = Media.find_many(
            field="sub",
            value=sub,
            limit=100
        )
        return media
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
