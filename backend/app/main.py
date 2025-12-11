from fastapi import FastAPI
from app.controllers import system_controller

app = FastAPI(title="Auto SRE Agent API")

# Include Routers
app.include_router(system_controller.router, prefix="/api/v1", tags=["System"])

@app.get("/")
async def root():
    return {"message": "Auto SRE Agent API is running"}
