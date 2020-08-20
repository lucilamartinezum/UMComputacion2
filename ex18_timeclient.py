import socket, getopt
from sys import argv, exit



def clientSTREAM(host, port):
    print("TCP Protocol Selected")
    host = host
    port = port
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        time = client.recv(1024).decode()
        try:
            print("Time:", time)
        except UnicodeDecodeError:
            print("Error of decoding")
    except socket.error:
        print("Failed to create socket", socket.error)
        exit()

def clientDGRAM(host, port):
    print("UDP Protocol Selected")
    host = host
    port = port
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto("".encode(), (host, port))
    except socket.error:
        print("Failed to create socket", socket.error)
        exit()
    client.sendto("".encode(), (host, port))
    time, addr = client.recvfrom(1024).decode()
    try:
        print("Time:", time)
    except UnicodeDecodeError:
        print("Error of decoding")

def main():
    def getOpts():
        try:
            (opts, args) = getopt.getopt(argv[1:], 'h:t:p:', [])
            return opts
        except getopt.GetoptError as err:
            print('Error: ' + str(err))
            exit()
    options = getOpts()
    for (opts, args) in options:
        if opts == '-p':
            port = int(args)
        if opts == '-t':
            protocol = args
        if opts == '-h':
            host = args

    if protocol == "tcp" or protocol == "TCP":
        clientSTREAM(host,port)
    elif protocol == "udp" or protocol == "UDP":
        clientDGRAM(host, port)
    else:
        print("Only enter 'UDP' or 'TCP'")

if __name__ == '__main__':
    main()