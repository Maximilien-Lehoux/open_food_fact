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
        self.cursor = self.connection.cursor()

    def create_tables(self):
        query = ''
        with open("data_base.sql", "r") as f:
            lines = f.readlines()
            query = " ".join(lines)
        try:
            for item in self.cursor.execute(query, multi=True):
                pass
        except RuntimeError:
            pass
        self.connection.commit()

    def insert_categories(self):
        i = 0
        while i < 5:
            self.cursor.execute("""INSERT INTO categories (name) VALUES(%s)""", (str(categories[i]),))
            i += 1
        self.connection.commit()

    def insert_products(self, name, generic_name, url, store, nutriscore):
        i = 0
        j = 1
        while i < number_products * number_categories:
            self.cursor.execute("""INSERT INTO products (name, generic_name, nutriscore, store, url, 
            categories_id) VALUES(%s, %s, %s, %s, %s, %s)""", (str(name[i]), str(generic_name[i]), str(nutriscore[i]),
                                                               str(url[i]), str(store[i]), j))
            i += 1
            if i == (number_products * j) and j < number_categories:
                j += 1
        self.connection.commit()
