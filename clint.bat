@echo off

:: Define variables
set "server_host=127.0.0.1"
set "server_port=12345"

:: Function to send information to the server
:send_info_to_server
powershell.exe -Command "while ($true) { $username = $env:USERNAME; $ip_address = (Test-Connection -ComputerName (hostname) -Count 1).IPV4Address.IPAddressToString; $message = 'User: ' + $username + ', IP: ' + $ip_address; Write-Output $message; $client = New-Object System.Net.Sockets.TcpClient; $client.Connect('%server_host%', %server_port%); $stream = $client.GetStream(); $writer = New-Object System.IO.StreamWriter($stream); $writer.WriteLine($message); $writer.Flush(); Start-Sleep -Seconds 5 }"
