import re


class PingParser(object):
    def parse(self, line):
        """
        Parse a line such as '64 bytes from 178.79.146.90: icmp_seq=3398 ttl=55 time=28.004 ms'
        into a struct such as ('178.79.146.90', 3398, 28.004).
        """
        pattern = re.compile(r'^\d+ bytes from ([0-9.]+): icmp_seq=(\d+) ttl=\d+ time=([0-9.]+) ms$')
        try:
            match = pattern.search(line)
            if not match:
                return
        except:  # resilient
            return
        ip, seq, time = str(match.group(1)), int(match.group(2)), float(match.group(3))
        return (ip, seq, time)
