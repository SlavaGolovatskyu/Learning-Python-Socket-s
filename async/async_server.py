import asyncio
from Socket_Async import Socket


class Server(Socket):
	def __init__(self):
		super(Server, self).__init__()

		self.users = []

	def set_up(self):
		self.socket.bind(('127.0.0.1', 9090))
		self.socket.listen(55)
		self.socket.setblocking(False)
		print('server listening')

	async def send_data(self, data=None):
		for user in self.users:
			await self.main_loop.sock_sendall(user, data)

	async def listen_socket(self, listened_socket=None):
		if listened_socket is None:
			return

		while True:
			data = await self.main_loop.sock_recv(listened_socket, 2048)
			print(f'user send {data}')
			await self.send_data(data)

	async def accept_sockets(self):
		while True:
			user_socket, address = await self.main_loop.sock_accept(self.socket)
			print(f'User {address[0]} connected')
			self.users.append(user_socket)
			self.main_loop.create_task(self.listen_socket(user_socket))

	async def main(self):
		await self.main_loop.create_task(self.accept_sockets())


if __name__ == '__main__':
	server = Server()
	server.set_up()

	server.start()


