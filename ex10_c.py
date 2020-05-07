
import os


def main():
    pipe_output = '/tmp/saludo'

    lines = ""

    fifo = open(pipe_output, 'r')
    lines = fifo.readlines()
    fifo.close()

    r, w = os.pipe()
    child = os.fork()

    if not child:

        os.close(w)
        read = open(r, 'r')
        saludo = read.readlines()
        print("Productor envía saludos: ")
        for line in saludo:
            print(line)
    else:
        os.close(r)
        write = open(w, 'w')
        write.writelines(lines)
        write.flush()
        write.close()


if __name__ == '__main__':
    main()
