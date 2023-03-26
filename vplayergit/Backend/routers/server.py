from fastapi import APIRouter
from datetime import datetime
import os

server_router = APIRouter()

@server_router.get("/server/scr")
async def server_check_readiness():
    return f'Server Running. Current Time: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'

@server_router.post("/server/cmd")
async def server_check_readiness(cmd: str):
    cmd = cmd.split("~")
    params = {}
    for commands in cmd:
        key, value = commands.split("=")
        params[key] = value
    if params.get("task", "RETURN") == "STOP":
        os.system("powershell .\stop.ps1")
    elif params.get("task", "RETURN") == "RESTART":
        os.system("powershell .\restart.ps1")