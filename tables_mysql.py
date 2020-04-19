import mysql.connector

from configuration import *
# from connection_mysql import *


class CreateDataBase:
    """allows you to create and display tables"""
    def __init__(self):
        self.connection = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DATABASE
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """creation of tables via sql file"""
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
        """the categories are inserted in the tables"""
        i = 0
        while i < 5:
            self.cursor.execute("""INSERT INTO categories (name) VALUES(%s)""", (str(CATEGORIES[i]),))
            i += 1
        self.connection.commit()

    def insert_products(self, name, generic_name, url, store, nutriscore):
        """the products are inserted in the tables"""
        i = 0
        j = 1
        while i < NUMBER_PRODUCTS * len(CATEGORIES):
            self.cursor.execute("""INSERT INTO products (name, generic_name, nutriscore, store, url, 
            categories_id) VALUES(%s, %s, %s, %s, %s, %s)""", (str(name[i]), str(generic_name[i]), str(nutriscore[i]),
                                                               str(url[i]), str(store[i]), j))
            i += 1
            if i == (NUMBER_PRODUCTS * j) and j < len(CATEGORIES):
                j += 1
        self.connection.commit()

    def saved_substitute(self, number_choice, product_id):
        """the products chosen by the user are saved in the table"""
        self.cursor.execute("""SELECT name FROM products WHERE id = {}""".format(number_choice))
        result = self.cursor.fetchone()
        for x in result:
            name_product = x
        self.cursor.execute("""INSERT INTO substitute_choose (products_id, substitute) VALUES(%s, %s)""",
                            (str(product_id), str(name_product)))
        print(name_product)
        self.connection.commit()

    def display_categories(self):
        """categories are displayed"""
        self.cursor.execute("""SELECT id, name  FROM categories""")
        result = self.cursor.fetchall()
        for x in result:
            print(x)

    def display_products(self, category_id):
        """products are displayed"""
        self.cursor.execute("""SELECT id, name, generic_name, nutriscore, store, url FROM products 
        WHERE categories_id = {}""".format(category_id))
        result = self.cursor.fetchall()
        for x in result:
            print(x)

    def display_substitutes(self, category_id):
        """Substitutes are displayed"""
        self.cursor.execute("""SELECT id, name, generic_name, nutriscore, store, url FROM products 
                WHERE categories_id = {} AND nutriscore = 'a'""".format(category_id))
        result = self.cursor.fetchall()
        for x in result:
            print(x)

    def display_substitute_saved(self):
        """saved substitutes are displayed"""
        print("Le premier produit noté entre guillemet est le substitut du deuxième :")
        self.cursor.execute("""SELECT substitute, name 
        FROM substitute_choose INNER JOIN products ON products_id = id""")
        result = self.cursor.fetchall()
        for x in result:
            print(x)