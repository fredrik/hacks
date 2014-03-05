import sys


def main():
    for line in lines(sys.stdin):
        print line.upper()


def lines(stream):
    buf = []
    while True:
        for character in stream.read(1):
            if character == '\n':
                yield "".join(buf)
                buf = []
            else:
                buf.append(character)


if __name__ == '__main__':
    main()
