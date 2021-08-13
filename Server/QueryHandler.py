import socket
from DatabaseConnector import Connector


class QueryHandler:

    def __init__(self):
        # initializing socket
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('192.168.1.86', 7676))
        self.socket.listen(5)  # setting socket to hold 5 sockets while working with one of them

        # initializing all socket variables
        self.connection = None
        self.address = None
        self.buffer_size = None
        self.data_receive = None

        # connector for sqlite
        self.db = Connector()

        # list for clients for each object
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

            # checking if query is the right type
            if len(self.data_receive.split('_')) == 4:
                self.db.connect('allq')
                self.db.write_query(self.data_receive)
                self.data_receive = self.data_receive.split('_')
                if self.data_receive[0] == '1':
                    try:
                        self.participants[self.data_receive[1]] += self.address
                    except KeyError:
                        self.participants[self.data_receive[1]] = self.address
            else:
                self.connection.send(b'Wrong query type')
