"""
@Author Erik Bjornoy
____________________
Python Module for creating Modbus TCP Server /  Modbus Slave
You must be on the same network as the device you are communicating with
"""


from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

class ModbusTCPServer(object):

	def __init__(self, host, port, no_block):
		"""
		Initiates modbus server and runs is.
		Set your own IP-Adresse as host, or "localhost"
		:param host: own IP-adresse
		:param port: port for modbus-communication
		"""

		self.host = host
		self.port = port
		self.no_block = no_block
		self.server = ModbusServer(self.host, self.port, self.no_block)


	def connectServer(self):
		"""
		Starts the server
		"""
		try:
			self.server.start()
		except Exception as e:
			raise Exception("Seems like the server can't assign the requested address. Try using sudo command.")


	def isConnected(self):
		"""
		Returns True if server is running
		"""

		return self.server.is_run
		print("Server is running..")


	def disconnect(self):
		"""
		Stops and disconnects the server
		Returns True if disconnected is successfull
		"""

		self.server.stop()
		return self.server.is_run

	def sendBool(self, register_adrs, value):
		"""
		Send boolean value
		register_adrs: adress to send value
		value: value to send -> True/False
		"""

		return DataBank.set_bits(address=register_adrs, bit_list=value)


	def readBool(self, register_adrs):
		"""
		Recive boolean value
		register_adrs: adresse to read from
		"""

		return DataBank.get_bits(address=register_adrs)


	def sendInt(self, register_adrs, value):
		"""
		Sends 32-bit integer value
		register_adrs: is the modbus adress to the recipients modbus-register.
		value: is the 32-bit value to send
		"""

		return DataBank.set_words(address=register_adrs, word_list=value)


	def readInt(self, register_adrs):
		"""
		Recive 32-bit integer value
		register_adrs: is the modbus register adress to read from
		"""
		return DataBank.get_words(address=register_adrs)


# if __name__=="__main__":
#
# 	print("Connecting to server.. ")
# 	print("Server started.. ")
# 	server = ModbusTCPServer("10.0.12.249", 502, True)	#10.0.12.101
# 	while server.isConnected():
#
# 		print(server.readInt(1000))
#
# 	print(server.isConnected())
# 	server.disconnect()
