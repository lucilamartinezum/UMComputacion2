import getopt, time
import socket
import sys

def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()

options = getOpts()
for (opts, args) in options:
    if opts == '-p':
        port = int(args)

def send(client_socket):
    while True:
        msg = input("\nAlice: ")
        if msg == 'cambio' or msg == 'CAMBIO':
            client_socket.send(msg.encode())
            time.sleep(2)
            break
        if msg == 'exit' or msg == 'EXIT':
            client_socket.send(msg.encode())
            exit()
        else:
            client_socket.send(msg.encode())

def to_Receive(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if data == 'cambio' or data == 'CAMBIO':
            print("\nBob:", data)
            break
        if data == 'exit' or data == 'EXIT':
            exit()
        else:
            print("\nBob:", data)


def walkie(c, addr):
    print("Address: %s " % str(addr))
    while True:
        to_Receive(c)
        send(c)

def createSocket(port):
    host = ""
    try:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as Err:
        print('Error:', Err)
        sys.exit()
    s_socket.bind((host, port))
    s_socket.listen(5)
    c_socket, addr = s_socket.accept()

    walkie(c_socket, addr)

if __name__ == '__main__':
    createSocket(port)
