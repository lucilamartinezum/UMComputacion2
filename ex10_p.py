import sys

def main():
    pipe_input = '/tmp/saludo'

    saludo = sys.argv[1:]

    fifo = open(pipe_input, "w")
    for line in saludo:
        fifo.write(line)
    fifo.flush()
    fifo.close()
    print("Mensaje de productor: ")
    for line in sys.argv[1:]:
        print(line)

if __name__ == '__main__':
    main()
