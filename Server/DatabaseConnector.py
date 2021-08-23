import sqlite3
import time


class Connector:

    def __init__(self):
        self.db_n_allq = 'db.sqlite'
        self.connection = None
        self.cursor = None

    def write_query(self, query):
        query = f'''INSERT INTO "all_queries" (id, query) VALUES ({int(time.time()*10000)}, "{query}")'''
        self.cursor.execute(query)
        self.connection.commit()

    def write_board(self, board_id, connection_types):
        query = f'''INSERT INTO "boards" (id, connection_types) VALUES ("{board_id}", "{connection_types}")'''
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('board is already in database')

    def get_board(self, board_id):
        query = f'''SELECT * FROM boards WHERE id="{board_id}"'''
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def connect(self):
        self.connection = sqlite3.connect(self.db_n_allq)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
