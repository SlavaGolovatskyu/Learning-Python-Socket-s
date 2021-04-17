import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
	msg = input('enter message: ')
	sock.send(f'{msg}'.encode())
	data = sock.recv(1024).decode()
	if msg == 'exit':
		sock.close()
		break
	print(data)