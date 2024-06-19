@echo off
setlocal

:: Define the service name and description
set "serviceName=MyPythonService"
set "serviceDisplayName=My Python Service"
set "serviceDescription=This service connects to a Python TCP server."

:: Path to Python executable and your Python script
set "pythonExePath=C:\Python\python.exe"
set "pythonScriptPath=E:\enchant\sbin\website(s)\YV-Ideology\SBFN\client.pyw"

:: Create a new service
powershell -Command "New-Service -Name %serviceName% -BinaryPathName '%pythonExePath% %pythonScriptPath%' -DisplayName %serviceDisplayName% -Description %serviceDescription%"

:: Start the service
powershell -Command "Start-Service -Name %serviceName%"
