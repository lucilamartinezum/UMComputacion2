import socket
import getopt
from sys import argv, exit


def main():
    def getOptions():
        try:
            (opts, arg) = getopt.getopt(argv[1:], 'p:h:', [])
            return opts
        except getopt.GetoptError as err:
            print('Error: ' + str(err))
            exit()

    options = getOptions()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)
        if opts == '-h':
            host = arg

    def createSocket(host, port):
        host = host
        port = port
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Failed to create socket")
            exit()
        s.connect((host, port))
        while True:
            try:
                msg = input("> ")
                if len(msg) != 0:
                    s.send(msg.encode('ascii'))
                    if msg == "exit":
                        print("Exit")
                        s.close()
                        break
                else:
                    print("Enter text:")
                msg = s.recv(2048)
                resp = msg.decode('ascii')
                print('--> ' + resp)


            except:
                pass

    createSocket(host, port)


if __name__ == '__main__':
    main()
