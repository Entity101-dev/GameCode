import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
	serv.bind((args.host, args.port))
	serv.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")

def on_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"THe new connection was made from IP: {ip}, and port: {port}!")
    conn, addr = serv.accept()
    while True:
        data = conn.recv(4096)
        if not data: break
        data2 = data.decode('utf-8')
        if data2 == "156":
            conn.send(bytes("Correct", "utf-8"))
        else:
            conn.send(bytes("Wrong", "utf-8"))
    conn.close()
    print('client disconnected')

while True:
	try: 
		client, ip = serv.accept()
		threading._start_new_thread(on_new_client,(client, ip))
		print("server started")
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this: {e}")
		break

sck.close()
