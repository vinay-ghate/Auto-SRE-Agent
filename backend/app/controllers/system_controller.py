from fastapi import APIRouter
from app.services.system_service import SystemService
from app.models.system_model import SystemStatus

router = APIRouter()

@router.get("/status", response_model=SystemStatus)
async def get_system_status():
    """
    Get current server status including process info, memory usage, and storage details.
    """
    return SystemService.get_system_status()
