import io
import pickle
import subprocess
from typing import Any

import httpx
import yaml
from fastapi import APIRouter, Body, HTTPException

router = APIRouter()


@router.post("/sandbox/exec")
async def run_customer_script(command: str = Body(embed=True)):
    """Dangerous debugging hook — shells out with operator-provided text."""
    completed = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {"stdout": completed.stdout, "stderr": completed.stderr, "code": completed.returncode}


@router.post("/bundle/import")
async def import_integration_bundle(blob: bytes = Body(...)):
    """Pickle handling on operator-supplied bytes — deserialization gap."""
    buffer = io.BytesIO(blob)
    manifest = pickle.load(buffer)
    return {"importedKeys": list(getattr(manifest, "keys", lambda: [])())}


@router.post("/template/render")
async def render_template_yaml(raw_yaml: str = Body(embed=True)):
    """YAML parsed without safe loader — demo anti-pattern."""
    structure: Any = yaml.load(raw_yaml, Loader=yaml.Loader)
    return {"keys": list(structure.keys()) if isinstance(structure, dict) else []}


@router.get("/market-data")
async def pull_market_data(url: str):
    """Server-side fetch to caller-controlled URL — SSRF-style integration."""
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url, timeout=15.0)
        if response.status_code >= 400:
            raise HTTPException(status_code=502, detail="Upstream error")
        return {"bytes": len(response.content)}
