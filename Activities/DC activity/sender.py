'''
Stop and wait protocol simulation
Sender's end
'''
import socket
from threading import *

sersock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
port = 8000

sersock.bind((host,port))

class client(Thread):
    def __init__(self,socket,address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
        
    def run(self):
        while 1:
            r = input("Enter data : ")
            clientsocket.send(r.encode())
            print(clientsocket.recv(1024).decode())


sersock.listen(5)
print ("Sender is ready and listening")
while True:
    clientsocket, address = sersock.accept()
    print("Receiver "+str(address)+ " connected")
    client(clientsocket,address)