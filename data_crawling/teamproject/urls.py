import urllib.parse as parse
import os.path as path

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)