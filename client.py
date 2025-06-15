import socket
pip install psutil
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the first variable specifies I am using ipv4, the second one specifies tcp
client.connect(('0.0.0.0', 8080))
#'0.0.0.0' connects you to the local computer, and you need to replace it with the server IP. 8080 is the port number
client.send(cpu_usage, memory_usage)
client.close()
#closes connection
