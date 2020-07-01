import socket
import argparse
import threading 

correct = 0



serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
	serv.bind(("0.0.0.0", 8080))
	serv.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")
print("server start")


def on_new_client(client, ip):
	while True:
		data = client.recv(4096)
		if not data: break
		print(data)
		if data == bytes("153", "utf-8"):
			print("wich is correct")
			client.send(bytes("Correct", "utf-8"))
			break
		else:
			client.send(bytes("Wrong", "utf-8"))
	client.close()
	print('client disconnected')

while True:
	try: 
		client, ip = serv.accept()
		on_new_client(client, ip)
		print("server started")
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this: {e}")
		break

client.close()
