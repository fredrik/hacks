import re
import sys
import subprocess


class Sha256Parser(object):

    pattern = re.compile(r'^SHA256 ?\((.+)\) ?= ?([0-9a-f]+)$')

    def parse(self, line):
        """
        Parse a line such as these:
        SHA256 (/tank/from-wd/Downloads-2012/Alva+Noto/Guest Appearance/Pomassl - Retrial Error - 2002 (CD - MP3 - V0 (VBR)).torrent) = 5749a31cb081064333782be3eaeae69d2c4a2674b57030423e2ffeee17d64cea
        SHA256(/Users/fredrik/.ssh/id_rsa.pub)= 8f6cfd1db5ff0aff84a5bbabd880da4bea22183ec721628d0b5c39d9b6add0eb

        The above are output from `sha256` (on FreeBSD) and `openssl dgst -sha256`.
        """
        try:
            match = self.pattern.search(line)
            if not match:
                return
        except:  # resilient
            return
        path, shasum = match.group(1), match.group(2)
        return path, shasum


def main():
    parser = Sha256Parser()
    for line in lines(sys.stdin):
        result = parser.parse(line)
        if not result:
            continue
        path, shasum = result
        print path, shasum
        subprocess.call("ls -lh {}".format(path), shell=True)


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
