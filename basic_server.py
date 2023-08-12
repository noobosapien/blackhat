#! /usr/bin/python3.S

import socket

class SP():
    def server(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("192.168.1.15", 1234))
            s.listen(1)

            while True:
                try:
                    c, addr = s.accept()
                    print("Got connection from", addr)

                    while True:
                        data = c.recv(1024)
                        if data:
                            d = data.decode('utf-8')
                            print("Got data: " + str(d))
                            c.send(str("ACK: " + str(d) + " ...").encode('utf-8'))
                        else:
                            print("No more data from client: " + str(addr))
                            break

                finally:
                    s.close()

        except Exception as ex:
            print("Exception caught: " + str(ex))
            s.close()

obj = SP()
obj.server()

