import sys
from datetime import datetime


def main():
    for line in lines(sys.stdin):
        now = datetime.utcnow()
        print now, line.upper()


def lines(stream):
    """
    Iterator over all lines of text in `stream`.
    (`stream` must be a file like object).
    """
    buf = []
    while True:
        character = stream.read(1)
        if character == "":
            return
        if character == '\n':
            yield "".join(buf)
            buf = []
        else:
            buf.append(character)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\ncaught CTRL-C'
