import socket
import asyncio

sock = socket.socket()

sock.bind(('', 9090))

# Колво подключений макс. Установленно на 1
# Если еще кто-то захочет подключить его пошлет.
sock.listen(10000)


async def connect():
	# Принимаем подключение клиента.
	conn, addr = sock.accept()
	print('connected: %s : %s' % addr)
	await return_message(conn, addr)


"""
Чтобы получить данные нужно воспользоваться методом recv, который в качестве 
аргумента принимает количество байт для чтения. Мы будем читать порциями по 1024 байт
"""

async def return_message(conn, addr):
	while True:
		await asyncio.sleep(3)
		data = conn.recv(1024)
		if data.decode() == 'exit':
			# Закрываем соединение.
			print('disconnected: %s : %s' % addr)
			break
		else:
			conn.send(data.upper())

asyncio.run(connect())

