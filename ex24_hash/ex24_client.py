import socket
import sys
import getopt

def getopts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:mt', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()

(option, value) = getopt.getopt(sys.argv[1:], "a:p:c:h:")
for (opt, val) in option:
    if opt == "-a":
        host = val
    if opt == "-p":
        port = int(val)
    if opt == "-c":
        text = val
    if opt == "-h":
        hash_type = val

def main(port, host, text, hash_type):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()

    s.connect((host, port))

    to_hash = text + "|" + hash_type
    s.send(to_hash.encode())

    response = s.recv(1024)
    print(response.decode())

    s.close()

if __name__ == '__main__':
    main(port, host, text, hash_type)



