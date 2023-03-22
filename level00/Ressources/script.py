"""
    This script collect list of files created by user,
    and decode content of it with help of
    Cesar's algorithm.
"""

from pathlib import Path
import paramiko
from cesardecode_lowercase import CesarDecoder
OwnerOfFile = 'flag00'

host = input("\033[92mEnter IP address of remote machine and press Return:\033[0m")
username = 'level00'
password = 'level00'

ssh = paramiko.SSHClient()
if ssh is not None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=username,password=password,port=4242)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f'find / -group {OwnerOfFile} 2>/dev/null')

    ListOfFiles = ssh_stdout.readlines()
    print("\033[95m", f"{username}'s files(green) and Cesar solution:", '\033[0m', '\n')
    tmp = None
    for file in ListOfFiles:
        print('\033[92m', '\t', file, '\033[0m')
        file_stdin, file_stdout, file_stderr = ssh.exec_command(f'cat {file}')
        ContentOfFile = file_stdout.readlines()
        if ContentOfFile != tmp: 
            for line in ContentOfFile:
                print('\033[93m', line, '\033[0m')
                CesarDecoder.DecodeThis(line)
            tmp =  ContentOfFile
        else:
            print('\033[93m', f'{line}', '\033[91mIt is the same content', '\033[0m')
        del file_stdin, file_stdout, file_stderr
        

    ssh.close()
    del ssh_stdin, ssh_stdout, ssh_stderr