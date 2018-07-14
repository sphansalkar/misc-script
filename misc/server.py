import socket, threading
import sys
import os
import pdb, time

server_address = './uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)

def test_thread(no):
    print("In thread %s" % no)
    time.sleep(no)

    return

while True:
    print("Wating for connection ...")

    connection, client_address = sock.accept()

    try:
        print("Connection from %s" % client_address)
        time.sleep(10)
        print("After Sleep >>>")

        thread_list = []

        for i in range(3):
            t = threading.Thread(target=test_thread, args=(i,))
            thread_list.append(t)
            t.start()

        for t in thread_list:
            t.join()
            print("After join ...")

    finally:
        connection.close()
