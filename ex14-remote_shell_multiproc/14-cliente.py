import socket
import sys
import getopt
import datetime

def main():
    (option, arg) = getopt.getopt(sys.argv[1:], "l:")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()
    host = "0.0.0.0"
    port = 8200
    s.connect((host, port))
    print("COMMAND PROMPT\n")
    command = ""
    while command != 'exit':
        command = input('Command: ')
        msg = command
        s.send(msg.encode('ascii'))
        msg = s.recv(1024)
        print('Server reply: ' + msg.decode())

        for (opt, arg) in option:
            if opt == "-l":
                file_path = arg
                file = open(str(file_path), "a")
                datetime_today = datetime.datetime.today()
                file.writelines("\n" + str(datetime_today) + "\n" + msg.decode())
                file.close()
    exit()

if __name__ == '__main__':
    main()