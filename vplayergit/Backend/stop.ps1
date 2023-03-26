$pythonpid = Get-Process | Where-Object {$_.ProcessName -match "python"}
Stop-Process -Force $pythonpid