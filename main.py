import json
import requests
import mysql.connector
import mysql

from api_data import *
from constant import *
# from connection_mysql import *

from tables_mysql import *


class Main:

    def __init__(self):
        self.init_categories()

    def get_products_key_from_api(self):
        i = 0
        while i < 5:
            products = DataApi("{}{}".format(url_general, categories[i]))
            name_products = products.select_key(products.data['products'], 'product_name_fr',
                                                temporary_list_product_name)
            generic_name_products = products.select_key(products.data['products'], 'generic_name_fr',
                                                        temporary_list_generic_name)
            brands_products = products.select_key(products.data['products'], 'brands', temporary_list_brands)
            url_products = products.select_key(products.data['products'], 'url', temporary_list_url)
            stores_products = products.select_key(products.data['products'], 'stores', temporary_list_stores)
            nutrition_grade_fr_products = products.select_key(products.data['products'], 'nutrition_grade_fr',
                                                              temporary_list_nutrition)
            i += 1
        # print(name_products)

    def tables_open_food_fact(self):
        my_tables = CreateDataBase()
        my_tables.create_tables()
        my_tables.insert_categories()

    def init_categories(self):
        self.get_products_key_from_api()
        self.tables_open_food_fact()


if __name__ == "__main__":
    m = Main()










