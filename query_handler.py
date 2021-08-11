import socket
import rsa
import config as cf
import json
import time
import socket


class Server:

    def __init__(self, server_ip, port):

        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((str(server_ip), int(port)))
        self.socket.listen(5)
        self.connection = None
        self.address = None
        self.buffer_size = 0
        self.json_data = 0
        # unsafe but for now ok
        self.data_receive = "bdalbdald"

        self.customers = {}

    def main(self):
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

            self.data_receive = self.data_receive.replace('"{', '{').replace('}"', '}').replace('\\', '').replace('}"', '}')

            self.data_receive = json.loads(self.data_receive)

            print(time.time())
            print(self.data_receive)

            if self.data_receive['type'] == 'request':
                try:
                    self.customers[self.data_receive['data']['object_name']].append(self.address)
                except KeyError:
                    self.customers[self.data_receive['data']['object_name']] = [self.address]

            elif self.data_receive['type'] == 'data':
                if self.data_receive['data']['object_name'] in self.customers.keys():
                    for address_from_connection in self.customers[self.data_receive['data']['object_name']]:
                        try:
                            to_send = json.dumps(self.data_receive).encode()
                            print(str(len(to_send)).encode())
                            address = '.'.join([str(i) for i in address_from_connection][:3])
                            address = address[:-6]
                            print(address)
                            socket_for_app = socket.socket()
                            socket_for_app.connect((address, 6767))
                            socket_for_app.send(str(len(to_send)).encode())
                            socket_for_app.send(to_send)
                            print(f'socket to address {address} was sent')
                        except:
                            print('error connecting to', address)


            self.connection.close()


if __name__ == '__main__':
    a = Server('192.168.1.86', 6767)
    a.main()
