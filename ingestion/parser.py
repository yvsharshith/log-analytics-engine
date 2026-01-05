import re

def parse_log_line(line):
    log_pattern = r'^(?P<timestamp>\S+\s+\S+) (?P<level>\S+) (?P<service>\S+) (?P<message>.*)$'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    else:
        return None
