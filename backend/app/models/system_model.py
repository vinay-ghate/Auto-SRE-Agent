from pydantic import BaseModel
from typing import Dict, Any

class ProcessInfo(BaseModel):
    pid: int
    name: str
    status: str

class MemoryInfo(BaseModel):
    total: int
    available: int
    percent: float
    used: int
    free: int

class StorageInfo(BaseModel):
    total: int
    used: int
    free: int
    percent: float

class SystemStatus(BaseModel):
    process: ProcessInfo
    memory: MemoryInfo
    storage: StorageInfo
