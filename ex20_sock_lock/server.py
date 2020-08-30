import multiprocessing as mp
import getopt
import sys
import socket
import pathlib


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

def handleFile(lock, clientsocket, address, serversocket, fileisopen):

    print("Connection:", address)
    while True:
        command = clientsocket.recv(1024).decode()
        try:
            if command == "OPEN":
                clientsocket.send("Enter file:".encode("ascii"))
                filename = clientsocket.recv(1024).decode("ascii")

                file = open(filename, "a")

                fileisopen = 1
                pathfile = str(pathlib.Path(filename).absolute())
                clientsocket.send(("File opened in:" +pathfile).encode("ascii"))


            if fileisopen == 1:

                    if command == "CLOSE":
                        lock.acquire()
                        file.close()
                        lock.release()
                        clientsocket.send("Closed".encode())


                    elif command == "ADD":
                        clientsocket.send("Enter text:".encode())
                        text = clientsocket.recv(1024).decode()
                        lock.acquire()
                        file = open(filename, "a")
                        file.writelines(text)
                        file.flush()
                        lock.release()
                        clientsocket.send("Added!".encode())
                    elif command == "READ":
                        file=(open(filename, "r"))
                        lock.acquire()
                        lines = file.readlines()
                        lock.release()
                        message = "Message: \n"
                        for line in lines:
                            message = message + line
                        clientsocket.send(message.encode("ascii") + "\nReading done!\n".encode("ascii"))
                    else:
                        clientsocket.send("\n***Enter READ, CLOSE OR ADD****\n".encode('ascii'))

            else:
                clientsocket.send("You must open a file.".encode('ascii'))
            if command == "exit":
                serversocket.close()
                break

        except Exception:
            clientsocket.send("Try with OPEN.\n".encode())

def createSocketTCP(port):
    port = port
    host = ""
    lock = mp.Lock()
    fileisopen = 0
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        clientsocket, address = serversocket.accept()
        child = mp.Process(target=handleFile, args=(lock, clientsocket, address, serversocket, fileisopen))
        child.start()


if __name__ == "__main__":
    createSocketTCP(port)

