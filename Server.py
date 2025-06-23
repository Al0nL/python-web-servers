import socket
import pandas as pd
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#defines that the server will use ipv4 and that we will use tcp
serv.bind(('0.0.0.0', 8080))
#makes it so that if any client tries to communicate on port 8080, the server will listen
serv.listen(5)
#can backlog up to 5 connections while it handles others
while True:
  conn, addr = serv.accept()
#this starts an infinite loop where the server is waiting for clients to connect, conn is a socket object, and addr is the client address and port  
  from_client = []
  #holds all data received from the client
  while True:
    data = conn.recv(4096)
    if not data: break
#this loop receives data in chunks of 4096 bytes and if there is no data to receive it breaks off the loop
    from_client += data.decode('utf8')
  conn.close()
#closes connection
df = pd.dataframe(from_client)
df.append_to_excel_pandas('client_info', sheet_name = 'Sheet1', index = false)
