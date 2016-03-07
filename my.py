#!/user/bin/python

import socket
import asyncore

class EH(asyncore.dispatcher_with_send):
	def handle_read(self):
		data = self.recv(1024)
		if bytes('close'.encode('utf-8')) in data:
			self.close()
		if data:
			self.send(data)
			
class EServer(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('', 2222))
		self.listen(10)
	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print 'conn', addr
			handler = EH(sock)
			
server = EServer('', 2222)
asyncore.loop()
