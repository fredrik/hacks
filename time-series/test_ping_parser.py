from ping_parser import PingParser


def test_parse_basics():
    parser = PingParser()
    assert parser.parse(None) is None
    assert parser.parse("") is None
    assert parser.parse("garbage garbage garbage") is None


def test_parse_good_ping_line():
    parser = PingParser()
    line = '64 bytes from 178.79.146.90: icmp_seq=3398 ttl=55 time=28.004 ms'
    assert parser.parse(line) == ('178.79.146.90', 3398, 28.004)
