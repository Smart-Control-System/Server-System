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
        self.clients_requests = {}
        self.commands = {}

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
                data = self.data_receive.split('_')

                if data[0] == '0':
                    try:
                        self.connection.send(self.commands[data[1]].pop().encode('utf-8'))
                    except IndexError:
                        pass  # if there is no commands for object just do nothing
                    if data[1] in self.clients_requests.keys():
                        for address in self.clients_requests[data[1]]:
                            sock_for_client = socket.socket()
                            sock_for_client.connect((address, 6767))
                            sock_for_client.send(self.data_receive.encode('utf-8'))

                # if client need to get data from obj
                elif data[0] == '1':
                    # adding or deleting client
                    if data[2] == '1':
                        try:
                            self.clients_requests[data[1]] += self.address
                        except KeyError:
                            self.clients_requests[data[1]] = self.address
                    elif data[2] == '0':
                        try:
                            self.clients_requests[data[1]].remove(self.address)
                        except ValueError:
                            pass

                # if client need to send come setting command
                elif data[0] == '2':
                    try:
                        self.commands[data[1]] += data[3]
                    except KeyError:
                        self.commands[data[1]] = data[3]
                else:
                    print('Unexpected type of request\n'
                          'Probably sb trying to hack')

            else:
                self.connection.send(b'Wrong query type')
