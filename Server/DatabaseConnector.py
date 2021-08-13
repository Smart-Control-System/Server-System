import sqlite3
import time


class Connector:

    def __init__(self):
        self.db_n_allq = 'db.sqlite'
        self.connection = None
        self.cursor = None

    def write_query(self, query):
        query = f"""INSERT INTO all_queries (id, query) VALUES ({time.time()}, {query})"""
        self.cursor.execute(query)
        self.connection.commit()

    def connect(self, name):
        if name == 'allq':
            self.connection = sqlite3.connect(self.db_n_allq)
            self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
