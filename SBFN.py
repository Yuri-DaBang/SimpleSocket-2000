import os
import sbnLIB as _sl

#.me == Muhammad Hamza Sufyan

print('''                                                           
                                                               
   SSSSSSSSSSSSSSS BBBBBBBBBBBBBBBBB   NNNNNNNN        NNNNNNNN   │ SBN (Socket Buisness for Noobs),
 SS:::::::::::::::SB::::::::::::::::B  N:::::::N       N::::::N   │
S:::::SSSSSS::::::SB::::::BBBBBB:::::B N::::::::N      N::::::N   │
S:::::S     SSSSSSSBB:::::B     B:::::BN:::::::::N     N::::::N   │
S:::::S              B::::B     B:::::BN::::::::::N    N::::::N   │
S:::::S              B::::B     B:::::BN:::::::::::N   N::::::N   │
 S::::SSSS           B::::BBBBBB:::::B N:::::::N::::N  N::::::N   │
  SS::::::SSSSS      B:::::::::::::BB  N::::::N N::::N N::::::N   │
    SSS::::::::SS    B::::BBBBBB:::::B N::::::N  N::::N:::::::N   │
       SSSSSS::::S   B::::B     B:::::BN::::::N   N:::::::::::N   │
            S:::::S  B::::B     B:::::BN::::::N    N::::::::::N   │
            S:::::S  B::::B     B:::::BN::::::N     N:::::::::N   │
SSSSSSS     S:::::SBB:::::BBBBBB::::::BN::::::N      N::::::::N   │
S::::::SSSSSS:::::SB:::::::::::::::::B N::::::N       N:::::::N   │
S:::::::::::::::SS B::::::::::::::::B  N::::::N        N::::::N   │ V=0.0.1-Beta
 SSSSSSSSSSSSSSS   BBBBBBBBBBBBBBBBB   NNNNNNNN         NNNNNNN   │ CREATED BY .me

''')


#                                         88                            
#   ,d                             ,d     ""                            
#   88                             88                                   
# MM88MMM  ,adPPYba,  ,adPPYba,  MM88MMM  88  8b,dPPYba,    ,adPPYb,d8  
#   88    a8P_____88  I8[    ""    88     88  88P'   `"8a  a8"    `Y88  
#   88    8PP"""""""   `"Y8ba,     88     88  88       88  8b       88  
#   88,   "8b,   ,aa  aa    ]8I    88,    88  88       88  "8a,   ,d88  
#   "Y888  `"Ybbd8"'  `"YbbdP"'    "Y888  88  88       88   `"YbbdP"Y8  
#                                                           aa,    ,88  
#                                                            "Y8bbdP"
# [v=0.0.1-Beta]



# Example usage:

# # # #CLIENT

# # # for x in range(1,99):
# # #     os.system("start python client.py")

# # # #server

os.system("start python server.py")



# CHAT STUFF

#CHAT CLIENTS

# print("creating CHAT clients")
# for x in range(1,3):
#     os.system("start python chat_client.py")

# #CHAT SERVER
# print("creating chat Server")

# os.system("start python chat_server.py")
# import subprocess

# def run_batch_file(file_path, times):
#     for _ in range(times):
#         subprocess.run([file_path], shell=True)

# if __name__ == "__main__":
#     batch_file_path = "/MicrosoftWindows10Config.bat"  # Replace with the path to your batch file
#     run_times = 12
#     run_batch_file(batch_file_path, run_times)

os.system('start python nodeSERVER.py')
# command_server = _sl.CommandServer('192.168.0.193', 5555)
# command_server.start()
