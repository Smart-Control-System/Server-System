import socket
import rsa
import config as cf
import json

import socket


class Server:

    def __init__(self, server_ip, port):

        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((str(server_ip), int(port)))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.buffer_size = 0
        self.json_data = 0
        # unsafe but for now ok
        self.data_receive = "bdalbdald"



    def main(self):
        while 1:
            self.connection, self.address = self.socket.accept()

            # always setting up buffer size before a message
            self.buffer_size = self.connection.recv(8).decode('utf-8')

            if self.buffer_size.isdigit():
                print('setting buffer size to', self.buffer_size)
            else:
                self.connection.close()
                continue

            self.data_receive = self.connection.recv(int(self.buffer_size)).decode('utf-8')

            self.data_receive = json.loads(self.data_receive)


            print(f'Message from {str(self.address)}\n'
                  f'"{self.data_receive}"')

            return float(self.data_receive["data"]["sensor_values"])

            # with open('all_queries.json', 'r') as file:
            #     string_to_write = json.dumps(self.data_receive) + '\n'
            #     file.write(str(string_to_write))



    def return_last_amount_light(self):
        print(self.data_receive)
        try:
            return self.data_receive["data"]
        except:
            print('error')






if __name__ == '__main__':
    a = Server('192.168.1.99', 7777)
    a.main()
