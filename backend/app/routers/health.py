import shutil

from fastapi import APIRouter

from ..config import APP_VERSION, get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict:
    settings = get_settings()
    return {
        "status": "ok",
        "version": APP_VERSION,
        "chat_enabled": settings.chat_enabled,
        "llm_model": settings.llm_model if settings.chat_enabled else None,
        "tf_fmt": settings.enable_tf_fmt and shutil.which("terraform") is not None,
        "default_region": settings.default_region,
    }
