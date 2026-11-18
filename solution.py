import urllib.parse

def solve(value):
    return urllib.parse.urlencode(value, doseq=True)
