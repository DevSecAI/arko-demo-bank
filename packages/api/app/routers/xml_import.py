from io import BytesIO

from fastapi import APIRouter, UploadFile
from lxml import etree

router = APIRouter()


@router.post("/statement-xml")
async def import_statement_xml(file: UploadFile):
    """XML ingest using generic parser — XXE-style parser misconfiguration risk."""
    raw = await file.read()
    tree = etree.parse(BytesIO(raw))
    root = tree.getroot()
    return {"tag": root.tag}
