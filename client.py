import socket
import psutil
import json
while True:
  cpu_usage = psutil.cpu_percent(interval=1)
  memory_usage = psutil.virtual_memory().percent
  list_to_send = [cpu_usage, memory_usage]
  json_str = json.dumps(list_to_send)
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the first variable specifies I am using ipv4, the second one specifies tcp
  client.connect(('192.168.1.16', 8080))
#'0.0.0.0' connects you to the local computer, and you need to replace it with the server IP. 8080 is the port number
  client.send(json_str.encode('utf-8'))
  client.close()
#closes connection
