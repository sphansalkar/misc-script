from SimpleXMLRPCServer import SimpleXMLRPCServer
import json

def tgtd(json_data):
    print json_data
    print type(json_data)
    print type(json.loads(json_data))

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(tgtd, "tgtd")
server.serve_forever()
