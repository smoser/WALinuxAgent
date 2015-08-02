import sys

"""
Add alies for python2 and python3 libs and fucntions.
"""

if sys.version_info[0]== 3:
    import http.client as httpclient
    from urllib.parse import urlparse
    text = str
    bytebuffer = memoryview
elif sys.version_info[0] == 2:
    import httplib as httpclient
    from urlparse import urlparse
    text = unicode
    bytebuffer = buffer
else:
    raise ImportError("Unknown python version:".format(sys.version_info))
