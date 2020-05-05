import mysql.connector

from configuration import USER, PASSWORD, HOST, DATABASE, CATEGORIES, \
    NUMBER_PRODUCTS


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
            self.cursor.execute("""INSERT INTO categories (name) VALUES(%s)""",
                                (str(CATEGORIES[i]),))
            i += 1
        self.connection.commit()

    def insert_product(self, product):
        self.cursor.execute("""INSERT INTO Products (name, generic_name, url, 
        store, nutriscore, categories_id) 
        VALUES (%s, %s, %s, %s, %s, %s)""",
                            (str(product[0]), str(product[1]), str(product[2]),
                             str(product[3]), str(product[4]),
                             str(product[5])))
        self.connection.commit()

    def insert_products(self, products):
        for i in range(0, len(products)):
            self.insert_product(products[i])

    def saved_substitute(self, number_choice, product_id):
        """the products chosen by the user are saved in the table"""
        self.cursor.execute("""SELECT name FROM products WHERE id = {}"""
                            .format(number_choice))
        result = self.cursor.fetchone()
        for x in result:
            name_product = x
        self.cursor.execute("""INSERT INTO substitute_choose
        (products_id, substitute) VALUES(%s, %s)""",
                            (str(product_id), str(name_product)))
        print(name_product)
        self.connection.commit()

    def get_categories(self):
        self.cursor.execute("""SELECT id, name  FROM categories""")
        result = self.cursor.fetchall()
        return result

    def get_products_from_category(self, category_id):
        self.cursor.execute("""SELECT id, name, generic_name, nutriscore,
        store, url FROM products WHERE categories_id = {}"""
                            .format(category_id))
        result = self.cursor.fetchall()
        return result

    def get_substitutes(self, category_id):
        self.cursor.execute("""SELECT id, name, generic_name, nutriscore,
                store, url FROM products WHERE categories_id = {}
                AND nutriscore = 'a'""".format(category_id))
        result = self.cursor.fetchall()
        return result

    def get_substitutes_saved(self):
        self.cursor.execute("""SELECT substitute, name
            FROM substitute_choose INNER JOIN products ON products_id = id""")
        result = self.cursor.fetchall()
        return result

