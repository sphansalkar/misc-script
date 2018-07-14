import xmlrpclib
import json

ip = "192.168.3.207"
port = 32819

proxy = xmlrpclib.ServerProxy('http://%s:%s' % (ip, port))
print proxy
