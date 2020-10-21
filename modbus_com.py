#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modbus-communication. Sending and
receiving data.

"""

# Importing packages
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient







class ModbusClient(object):
    """Establishes a secure connection with the
    Modbus slave. Will be able to read and write
    to all of the available I/O."""

    def __init__(self, ip): 	# (self, ip='xxx.xxx.xxx'):
        self.ip = ip
        self.client = ModbusTcpClient(self.ip, 502)
        self.connection = self.client.connect()

    def isConnected(self):
        """Returns the connection status.
        Return: True if connected, False if not."""
        return self.connection
        print("Connection Success")

    def sendBool(self, adress, value):
        """Sends boolean value to given adress.
        Parameters: 
        adress: modbus adress to start transmitting to.
        value:  Value to send -> True og False. 
        Return: Result if it was successful or not. 
        """
        return self.client.write_coil(adress, value, unit=1)        # first parameter is amount of couls to read. 

    def sendInt(self, address, value):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not.
        """
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_int(value)
        payload = builder.build()
        
        return self.client.write_register(address, value, unit=1)


    def sendFloat(self, value, address):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not."""
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_float(value)
        payload = builder.build()
        result = self.client.write_registers(address, payload, skip_encode=True, unit=1)
        return result
    #
    #
    #

    def readBool(self, adress):
        """Reads a boolean value starting at given adress. 
        Parameter: What adress to start reading from.
        Returns the True of False  or   1 || 0 
        """
        return self.client.read_coils(adress)

    def readInt(self, address, size):
        """Reads the number of addresses that the size contains.
        The readings start from the given address.
        Return: An array of read values"""
        response = self.client.read_holding_registers(address, size, unit=1)
        return response.registers

    def readFloat(self, address, size):
        """Reads two bytes from the given start address.
        Returns the decoded float value"""
        response = self.client.read_holding_registers(address, size, unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(response.registers,
                                                     byteorder=Endian.Big,
                                                     wordorder=Endian.Little)
        value = decoder.decode_32bit_float()
        return value

    def close(self):
        """Closes the connection with the port.
        Return: True when the connection is closed."""
        self.client.close()
        return True


def start_demo_one(): 
    print("Demo 1 reached")
    client = ModbusClient(ip="10.0.12.50")
    while client.isConnected():
        client.sendBool(12288, True)
    client.close()
    

def stop_demo_one():
    
    while client.isConnected():
        client.sendBool(12288, False)
    client.close()
    


            
# Simple example of usage
if __name__ == '__main__':
    print("modbus reached")
    client = ModbusClient(ip="10.0.12.50")
    """
    while client.isConnected():
        client.sendBool(12288, True)
    client.close()
    """

    
    
    
    
    
    
    """
    client = ModbusClient(ip='10.0.12.50')

    while client.isConnected():
        print("Connected")
        client.sendBool(12288, True)
        print("Value is sent")
    
    client.close()
  
    """
      


        



 

