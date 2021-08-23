import socket


class ClientFunc:

    def __init__(self):

        self.server_ip = '10.0.0.200'
        self.server_port = 6767

    def get_board(self, board_id):

        send_sck = socket.socket()
        send_sck.connect((self.server_ip, self.server_port))
        print('connected to server')
        to_send = f'4_{board_id}'
        send_sck.send(len(to_send))
        send_sck.send(to_send.encode('utf-8'))
        print('request sent')
        buffer_size = send_sck.recv(8).decode('utf-8')
        if buffer_size.is_digit():
            pass
        else:
            send_sck.close()
            print('Error in getting data from server\n'
                  "(buffer_size isn't digit)")
        data_recieved = send_sck.recv(buffer_size).decode('utf-8')
        print('answer recieved')
        return data_recieved
