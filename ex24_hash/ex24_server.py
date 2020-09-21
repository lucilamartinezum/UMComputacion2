import getopt
import socket
import sys
import threading as th
import multiprocessing as mp
import hashlib

multiprocessing = False
threading = False

def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:mt', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()

options = getOpts()
for (opts, args) in options:
    if opts == '-p':
        port = int(args)
    if opts == '-m':
        multiprocessing = True
    if opts == '-t':
        threading = True

def hash(t, h, clientsocket):
    t = t.encode()
    h = hashlib.new(h, t)  #retorna un nuevo objeto de la clase hash implementando la función (hash) especificada.
    msg = h.hexdigest()
    print(msg)
    clientsocket.send(msg.encode())

def receive(clientsocket, address):
    print("Address: %s " % str(address))
    data = clientsocket.recv(1024).decode()
    data = data.split("|")
    text = str(data[0])
    print(text)
    hash_type = str(data[1])
    hash(text, hash_type, clientsocket)




def createSocket_mp(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    serversocket.bind((host, port))
    serversocket.listen(5)
    print('Server waiting for clients...')
    while True:
        clientsocket, addr = serversocket.accept()
        p = mp.Process(target=receive, args=(clientsocket, addr))
        p.start()

def createSocket_th(port):
    host = ""
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as Err:
        print('Error:', Err)
        sys.exit()
    serversocket.bind((host, port))
    serversocket.listen(5)
    print('Server waiting for clients...')
    while True:
        clientsocket, addr = serversocket.accept()
        thread = th.Thread(target=receive, args=(clientsocket, addr))
        thread.start()

def main():
    if multiprocessing:
        createSocket_mp(port)
    if threading:
        createSocket_th(port)

if __name__ == '__main__':
    main()