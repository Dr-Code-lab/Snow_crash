"""
    This script help to find password from hex code of tcp trace log
"""

from asyncio import streams
from tkinter import N, Y
import paramiko
from os import path, system
from warnings import filterwarnings
filterwarnings("ignore")

host = input("\033[92mEnter IP address of remote machine and press Return:\033[0m")
username = 'level02'
password = 'f2av5il02puano7naaf6adaaf'

ssh = paramiko.SSHClient()
if ssh is not None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=username,password=password,port=4242)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    ls = ssh_stdout.readlines()
    filename = f'{ls[0][0:-1]}'
    print("\033[95m", '\n', f"""Content of user's home directory:\n
            \033[96m {filename}\n\n Here it is! Just need some hack!\n""", '\033[0m')

    # get file from remote machine
    ftp = ssh.open_sftp()
    ftp.get(filename, f'./{filename}')
    ftp.close()

    del ssh_stdin, ssh_stdout, ssh_stderr
    ssh.close()

    system(f"tshark -r  {filename}  -z follow,tcp,hex,0")

    print("\n\033[96mASCI table:\033[0m\n")
    system("man ascii | cut -d~ -f2 | grep 7f")
else :
    print("Install wireshark first")

  
    




    

    