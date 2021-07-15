import socket
import rsa
import config as cf
import json

import socket


class Server:

    def __init__(self, server_ip, port):

        self.socket = socket.socket()
        self.socket.bind((str(server_ip), int(port)))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.buffer_size = 0
        self.json_data = 0

    def main(self):
        try:
            while 1:
                self.connection, self.address = self.socket.accept()
                print(self.connection)

                # always setting up buffer size before a message
                self.buffer_size = self.connection.recv(8).decode('utf-8')

                if self.buffer_size.isdigit():
                    print('setting buffer size to', self.buffer_size)
                else:
                    self.connection.close()
                    continue

                data_receive = self.connection.recv(int(self.buffer_size)).decode('utf-8')

                data_receive = json.loads()

                with open('all_queries.json', 'r') as file:
                    string_to_write = data_receive + '\n'
                    file.write(string_to_write)

                print(f'Message from {str(self.address)}\n'
                      f'"{data_receive}"')

        except Exception as ex:
            print(ex)
        finally:
            self.socket.close()




if __name__ == '__main__':
    a = Server('192.168.1.86', 7777)
    a.main()
