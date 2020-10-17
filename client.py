import socket
import time


class SocketClient:
    DISCONNECT_MESSAGE = '!DISCONNECT'
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    SERVER = '192.168.0.14'
    ADDR = (SERVER, PORT)
    connected = False
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        print('trying to connect')
        try:
            self.client.connect(self.ADDR)
            self.connected = True
        except:
            self.connected = False
            print('connection failed')

    def sendMessage(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def send(self, msg):
        if not self.connected:
            self.connect()

        if self.connected and msg != self.DISCONNECT_MESSAGE:
            self.sendMessage(msg=msg)
            return True
        elif msg == self.DISCONNECT_MESSAGE and self.connected:
            self.sendMessage(msg=self.DISCONNECT_MESSAGE)
            self.connected = False
            self.client.close()
            return True
        else:
            return False
