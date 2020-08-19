import socket
import getopt
import sys
import multiprocessing as mp

def reverseMessage(clientsocket, addr):
    print(addr)
    while True:
        data = clientsocket.recv(1024)
        print("Address: %s " % str(addr))
        msg = data.decode("ascii")
        print("Recibido: " + msg)
        resp = msg[::-1]
        print(resp)
        clientsocket.send(resp.encode('ascii'))
        if data.decode('ascii') == 'exit':
            clientsocket.close()
            print("Goodbye! %s " % str(addr))
            exit(-1)

def main():
    def getOpts():
        try:
            (opts, arg) = getopt.getopt(sys.argv[1:], 'p:', [])
            return opts
        except getopt.GetoptError as err:
            print('Error: '+str(err))
            exit()
    options = getOpts()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)
        else:
            print("Wrong parameters")
            exit(-1)

    def createSocket(port):
        port = port
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        serversocket.bind((host, port))
        serversocket.listen(5)
        print('Server waiting for clients...')
        while True:
            clientsocket, addr = serversocket.accept()
            child = mp.Process(target=reverseMessage, args=(clientsocket, addr))
            child.start()

    createSocket(port)

if __name__ == '__main__':
    main()