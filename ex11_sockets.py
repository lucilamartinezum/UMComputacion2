import sys
import socket
import getopt



def main():
    host = None
    port = None
    code = None

    def reply():
        if respuesta == 200:
            print("Server reply: 200 - OK")
        elif respuesta == 400:
            print("Server reply: 400 - Comando válido, pero fuera de secuencia.")
        elif respuesta == 500:
            print("Server reply: 500 - Comando invalido")
        elif respuesta == 404:
            print("Server reply: 404 - Clave erronea")
        elif respuesta == 405:
            print("Server reply: 405 - Cadena nula")

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:', ["host=", "port="])
    except getopt.GetoptError as err:
        print("ERROR", str(err))
        exit()
    for (option, arg) in opt:
        if option == '-h' or option == '--host':
            host = arg
        elif option == '-p' or option == '--port':
            port = int(arg)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()

    s.connect((host, port))
    print("CONNECTED")

    while True:

        msgin = input('ENTER NAME : ')
        try:
            # enviar mensaje str
            msg = 'hello|' + msgin
            s.send(msg.encode('ascii'))

            # recibir data
            resp = s.recv(1024)
            respuesta = int(resp.decode("ascii"))
            reply()

        except socket.error:
            print('CODIGO DE ERROR> : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        msgin = input('ENTER EMAIL : ')
        try:
            # enviar mensaje str
            msg = 'email|' + msgin
            s.send(msg.encode('ascii'))

            # recibir data
            resp = s.recv(1024)
            respuesta = int(resp.decode("ascii"))
            reply()

        except socket.error:
            print('CODIGO DE ERROR> : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        while not code == 200:
            msgin = input('ENTER KEY : ')
            msg = 'key|' + msgin
            s.send(msg.encode('ascii'))

            # recibir data
            resp = s.recv(1024)
            respuesta = int(resp.decode("ascii"))
            code = respuesta
            reply()

        msg = 'exit'.encode()
        try:
            print("SENDING EXIT")
            s.sendto(msg, (host, port))
            respuesta = s.recv(1024)

            print('RESPUESTA DEL SV: ' + respuesta.decode("ascii"))
            sys.exit()

        except socket.error:
            print('CODIGO DE ERROR> ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

    s.close()
if __name__ == '__main__':
        main()
