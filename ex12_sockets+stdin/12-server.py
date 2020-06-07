import socket
import getopt
import sys


def main():
    def getOpts():
        try:
            (opts, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:', [])
            return opts
        except getopt.GetoptError as err:
            print('Error: '+str(err))
            exit()


    options = getOpts()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)
        if opts == '-t':
            protocol = arg
        if opts == '-f':
            pathfile = arg


    def createSocket(port, protocol, pathfile):
        port = port
        protocol = protocol
        file = pathfile

        if protocol == 'tcp' or protocol == 'TCP':
            print('TCP Protocol')
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = ""
            serversocket.bind((host, port))
            serversocket.listen(5)
            print('Server waiting for clients...')
            clientsocket, addr = serversocket.accept()
            while True:
                f = open(file, "a")
                d = clientsocket.recv(1024)
                f.write(d.decode("ascii")+'\n')
                if d == "" or len(d) == 0:
                    print('Exit')
                    break
                print("Address: %s " % str(addr))
                print("Received correctly: "+d.decode("ascii"))


        elif protocol == 'udp' or protocol == 'UDP':
            print('UDP Protocol')
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host = ""
            serversocket.bind((host, port))
            print('Server waiting for clients...')
            while True:
                f = open(file, "a")
                d, addr = serversocket.recvfrom(1024)
                f.write(d.decode("ascii")+'\n')
                address = addr[0]
                port = addr[1]
                if d == "" or len(d) == 0:
                    print('Exit')
                    break
                print("Address: %s - Port %d" % (address, port))
                print("Received correctly: "+d.decode("ascii"))


        else:
            print('Invalid protocol')

    createSocket(port, protocol, pathfile)

if __name__ == '__main__':
        main()
