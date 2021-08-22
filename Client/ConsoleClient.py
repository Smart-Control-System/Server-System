import os
import time
from Board import Board
from CLientFunxionality import ClientFunc



class ConsoleClient:

    def __init__(self):
        self.added_boards = []

        self.flag_add_new_board = True

        self.start()

    def start(self):

        print('#####################################################\n'
              '#                                                   #\n'
              '#                                                   #\n'
              '#                   Welcome to SCS                  #\n'
              '#               (smart control sysytem)             #\n'
              '#                                                   #\n'
              '#####################################################')

        if self.added_boards:
            self.choose_board()
        else:
            if self.flag_add_new_board:
                print('You have no boards connected\n'
                      'Do you want to add one?Y\\n')
                ans = input()

                if ans == 'y' or ans == 'Y':
                    print('Going to adding boards menu')
                    for i in range(1, 4):
                        print('.' * i, end='\r')
                        time.sleep(1)
                    self.add_board()

                elif ans == 'n' or ans == 'N':
                    print('ok, you can stay and stick to the screen')
                    time.sleep(2)
                    self.flag_add_new_board = False
                    os.system('cls')
                    self.start()

                else:
                    self.start()
            else:
                input()

    def add_board(self):
        os.system('cls')
        board_id = input('Enter the board id: ')
        if board_id not in [i.id for i in self.added_boards]:
            print('Adding the new board')


    def choose_board(self):
        pass


if __name__ == '__main__':
    a = ConsoleClient()
