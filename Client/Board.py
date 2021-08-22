import config as cf


class Board:

    def __init__(self, board_id, connections):

        self.id = board
        self.sensors = {}
        for conn in connections:
            self.sensors[cf.conn_defenitions[conn]] = 0

    def update_values(self):
        pass
