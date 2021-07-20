import socket
import time
import json
import random

class Client:

    def __init__(self):
        self.socket_start = socket.socket()
        self.socket = socket.socket()

    def main(self, param):
        if param == 'station':
            self.socket_start.connect(('192.168.1.86', 6767))
            request = {'type': 'request',
                       'data': {'object_name': 'station_0'}
                       }
            self.socket_start.send(str(len(json.dumps(request).encode())).encode())
            self.socket_start.send(json.dumps(request).encode())

        print('socket sent')
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('192.168.1.100', 6767))
        self.socket.listen(1)
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
            print(f'Message from {str(self.address)}\n'
                  f'{self.data_receive}')

            self.data_receive = json.loads(self.data_receive.replace('\\', ''))



            # self.data_receive = str(random.randint(1, 100))

            def write_fake_data(filename, data):

                with open(filename, 'r') as file:
                    readed = file.read().split("__")
                with open(filename, 'w') as file:
                    readed.reverse()
                    readed.append(data)
                    readed.reverse()

                    if len(readed) > 10:
                        readed = readed[:10]

                    file.write('__'.join(readed))

            if self.data_receive["data"]["sensor_type"] == "light":
                write_fake_data('light_sensor', self.data_receive["data"]["values"])
            elif self.data_receive["data"]["sensor_type"] == "dht11":
                write_fake_data('dht_11_temp', self.data_receive["data"]["values"]["temp"])
                write_fake_data('dht_11_wet', self.data_receive["data"]["values"]["wet"])

    def stop_conection(self):
        self.socket.close()



if __name__ == "__main__":
    client = Client()
    client.main('station')
