from fastapi import APIRouter, UploadFile, File, Form
import os
from os import getcwd, remove
from fastapi.responses import FileResponse, JSONResponse
from shutil import rmtree

router = APIRouter()

directory = getcwd() + "/files/"

@router.post("/uploadFile")
async def upload_file(file: UploadFile = File(...)):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return "success"

@router.get("/file/{filename}")
def get_file_by_name(filename: str):
    return FileResponse(directory + filename)

@router.get("/download_file/{filename}")
def get_download_file_by_name(filename: str):
    print(filename)
    return FileResponse(directory + filename, media_type="application/octet-stream", filename=filename)

@router.delete("/delete_file/{filename}")
def delete_file_by_name(filename: str):
    try:
        remove(directory + filename)
        return JSONResponse(content={"removed": True}, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"removed": False, "msg": "File not found"}, status_code=404)

@router.delete("/delete_folder")
def delete_file_by_name(folder: str = Form(...)):
    try:
        rmtree(getcwd() + folder)
        return JSONResponse(content={"removed": True}, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"removed": False, "msg": "Folder not found"}, status_code=404)