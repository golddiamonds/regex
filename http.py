import re

#regex of common protocols
http_regex = re.compile(r"(http://|https://|ftp://)")

m = http_regex.match("http://")

#print entire match
print m.group(0)


