import socket
from DatabaseConnector import Connector


class QueryHandler:

    def __init__(self):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('192.168.1.86', 7676))
        self.socket.listen(5)

        self.connection = None
        self.address = None
        self.buffer_size = None
        self.data_receive = None

        self.db = Connector()

        self.participants = {}

    def mainloop(self):
        while 1:
            self.connection, self.address = self.socket.accept()
            # always setting up buffer size before a message
            self.buffer_size = self.connection.recv(8).decode('utf-8')

            if self.buffer_size.isdigit():
                pass
            else:
                self.connection.close()
                continue

            self.data_receive = self.connection.recv(int(self.buffer_size)).decode('utf-8')

            if len(self.data_receive.split('_')) == 4:
                self.db.connect('allq')
                self.db.write_query(self.data_receive)
                self.data_receive = self.data_receive.split('_')
                if self.data_receive[0] == '1':

            else:
                self.connection.send(b'Wrong query type')
