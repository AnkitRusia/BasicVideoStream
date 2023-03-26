
$pythonpid = Get-Process | Where-Object {$_.ProcessName -match "python"}
Stop-Process -Force $pythonpid


.\venv\Scripts\Activate.ps1
python31 -m uvicorn main:app