import psutil
import os
from app.models.system_model import SystemStatus, ProcessInfo, MemoryInfo, StorageInfo

class SystemService:
    @staticmethod
    def get_system_status() -> SystemStatus:
        # Current Process Info
        pid = os.getpid()
        process = psutil.Process(pid)
        process_info = ProcessInfo(
            pid=pid,
            name=process.name(),
            status=process.status()
        )

        # Memory Info
        mem = psutil.virtual_memory()
        memory_info = MemoryInfo(
            total=mem.total,
            available=mem.available,
            percent=mem.percent,
            used=mem.used,
            free=mem.free
        )

        # Storage Info
        # Get disk usage of the current working directory's drive
        disk = psutil.disk_usage(os.getcwd())
        storage_info = StorageInfo(
            total=disk.total,
            used=disk.used,
            free=disk.free,
            percent=disk.percent
        )

        return SystemStatus(
            process=process_info,
            memory=memory_info,
            storage=storage_info
        )
