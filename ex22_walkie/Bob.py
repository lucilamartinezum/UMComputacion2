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

def send(server_socket):
    while True:
        msg = input("\nBob: ")
        if msg == 'cambio' or msg == 'CAMBIO':
            server_socket.send(msg.encode())
            time.sleep(2)
            break
        if msg == 'exit' or msg == 'EXIT':
            server_socket.send(msg.encode())
            exit()
        else:
            server_socket.send(msg.encode())

def to_Receive(server_socket):
    while True:
        data = server_socket.recv(1024).decode()
        if data == 'cambio' or data == 'CAMBIO':
            print("\nAlice:", data)
            break
        if data == 'exit' or data == 'EXIT':
            exit()
        else:
            print("\nAlice:", data)

def walkie(server_s):
    while True:
        send(server_s)
        to_Receive(server_s)

def createSocket(port):
    host = ""
    try:
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as Err:
        print('Error:', Err)
        sys.exit()
    s_socket.connect((host, port))

    walkie(s_socket)

if __name__ == '__main__':
    createSocket(port)
