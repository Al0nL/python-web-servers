import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the first variable specifies I am using ipv4, the second one specifies tcp
client.connect(('0.0.0.0', 8080))
#'0.0.0.0' connects you to the local computer, and you need to replace it with the server IP. 8080 is the port number
client.send("I am CLIENT\n".encode())
#transmits from the client 'I am client' encoded in bytes, since that is what TCP transfers
from_server = client.recv(4096)
#tells client, my computer, to wait and receive up to 4096 bytes of data from the server
client.close()
#closes connection
