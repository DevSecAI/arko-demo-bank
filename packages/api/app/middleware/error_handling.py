import traceback

from fastapi import Request
from fastapi.responses import JSONResponse


async def debug_exception_handler(request: Request, exc: Exception):
    """Returns stack traces to API consumers — operational leak."""
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_error",
            "detail": str(exc),
            "trace": traceback.format_exc(),
            "path": str(request.url.path),
        },
    )
