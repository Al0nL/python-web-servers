import socket
import json
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "computer_info"
headers = ["cpu utilization", "memory utilization"]
ws.append(headers)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#defines that the server will use ipv4 and that we will use tcp
serv.bind(('192.168.1.16', 8080))
#makes it so that if any client tries to communicate on port 8080, the server will listen
serv.listen(5)
#can backlog up to 5 connections while it handles others
while True:
    conn, addr = serv.accept()
    print(f"Connected by {addr}")

    try:
        received_bytes = conn.recv(1024)
        if not received_bytes:
            continue  # no data received, go back to listening

        received_list = json.loads(received_bytes.decode('utf-8'))

        # Append to Excel
        ws.append(received_list)
        wb.save("computer_info.xlsx")
        print("Data saved.")

    except Exception as e:
        print(f"Error handling client {addr}: {e}")

    finally:
        conn.close()
