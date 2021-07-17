import socket
import time
import json
import random

class Client:

    def __init__(self, server_ip, port):
        # self.socket = socket.socket()
        # self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.socket.bind((str(server_ip), int(port)))
        # self.socket.listen(1)
        # self.connection = None
        # self.address = None
        # self.buffer_size = 0
        # self.json_data = 0
        # # unsafe but for now ok
        # self.data_receive = "bdalbdald"
        self.a = 1

    def main(self):
        while 1:
            # self.connection, self.address = self.socket.accept()
            #
            # # always setting up buffer size before a message
            # self.buffer_size = self.connection.recv(8).decode('utf-8')
            #
            # if self.buffer_size.isdigit():
            #     print('setting buffer size to', self.buffer_size)
            # else:
            #     self.connection.close()
            #     continue
            #
            # self.data_receive = self.connection.recv(int(self.buffer_size)).decode('utf-8')
            #
            # self.data_receive = json.loads(self.data_receive)
            #
            # print(f'Message from {str(self.address)}\n'
                #       f'"{self.data_receive}"')
                def write_fake_data(filename):
                self.data_receive = str(random.randint(1, 100))

                with open(filename, 'r') as file:
                    readed = file.read().split("__")
                with open(filename, 'w') as file:
                    print(readed)
                    readed.reverse()
                    readed.append(self.data_receive)
                    readed.reverse()

                    if len(readed) > 10:
                        readed = readed[:10]

                    file.write('__'.join(readed))
            write_fake_data('random_1')
            write_fake_data('random_2')
            write_fake_data('random_3')

            time.sleep(1)



if __name__ == "__main__":
    client = Client('192.168.1.100', 6767)
    client.main()
