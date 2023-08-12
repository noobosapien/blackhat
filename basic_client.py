#! /usr/bin/python3.S

import socket

class SP():
    def client(self):
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.1.15', 80))

            while True:
                data = input("Enter data for the server: \n")

                if not data:
                    break
                else:
                    s.send(data.encode('utf-8'))
                    reply = s.recv(1024).decode('utf-8')
                    print(str(reply))


                s.close()
        except Exception as ex:
            print("Exception caught: " + str(ex))
    
obj = SP()
obj.client()
