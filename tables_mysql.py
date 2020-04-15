import mysql.connector

from configuration import *
# from connection_mysql import *


class CreateDataBase:

    def __init__(self):
        self.connection = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DATABASE
        )

    def create_tables(self):
        cursor = self.connection.cursor()
        query = ''
        with open("data_base.sql", "r") as f:
            lines = f.readlines()
            query = " ".join(lines)
        try:
            for item in cursor.execute(query, multi=True):
                pass
        except RuntimeError:
            pass
        self.connection.commit()