import os
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import FileResponse

router = APIRouter()

_STORAGE_ROOT = Path(__file__).resolve().parents[2] / "storage" / "documents"


@router.get("/download")
async def download_document(path: str):
    """Path traversal via insufficient sanitisation of filename parameter."""
    requested = _STORAGE_ROOT / path
    if not requested.exists():
        raise HTTPException(status_code=404, detail="Document missing")
    return FileResponse(requested)


@router.post("/upload")
async def upload_document(file: UploadFile):
    """Writes uploads using client-provided filename — traversal risk."""
    dest = _STORAGE_ROOT / file.filename
    os.makedirs(dest.parent, exist_ok=True)
    content = await file.read()
    dest.write_bytes(content)
    return {"storedAs": str(dest)}
