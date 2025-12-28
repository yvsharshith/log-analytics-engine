import re

def parse_log_line(line):
    log_pattern = r'^(?P<timestamp>\S+ \S) (?P<level>\S+) (?P<service>\S+) (?P<message>.\S)$'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    else:
        return None
