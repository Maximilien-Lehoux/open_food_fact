import mysql.connector
import mysql
import sys

from api_data import *
from constant import *
from menu import *
from tables_mysql import *


class Main:

    def __init__(self):
        self.init_program()

    def get_products_key_from_api(self):
        i = 0
        while i < 5:
            products = DataApi("{}{}".format(url_general, categories[i]))
            self.name_products = products.select_key(products.data['products'], 'product_name_fr',
                                                     temporary_list_product_name)
            self.generic_name_products = products.select_key(products.data['products'], 'generic_name_fr',
                                                             temporary_list_generic_name)
            self.url_products = products.select_key(products.data['products'], 'url', temporary_list_url)
            self.store_products = products.select_key(products.data['products'], 'stores', temporary_list_stores)
            self.nutriscore_products = products.select_key(products.data['products'], 'nutrition_grade_fr',
                                                           temporary_list_nutrition)
            i += 1

    def create_tables_open_food_fact(self):
        my_tables = CreateDataBase()
        my_tables.create_tables()
        my_tables.insert_categories()
        my_tables.insert_products(self.name_products, self.generic_name_products,
                                  self.url_products, self.store_products, self.nutriscore_products)

    def display_data_open_food_fact(self):
        my_menu = Menu()
        my_data = CreateDataBase()
        main_choice = my_menu.main_menu()

        if main_choice == "1":

            my_data.display_categories()

            category_choice = my_menu.menu_category()
            my_data.display_products(category_choice)

            number_products_choice = my_menu.menu_products()
            my_data.display_substitutes(category_choice)

            print(number_products_choice)
            number_substitute_choiced = my_menu.menu_choice_substitute()
            my_data.saved_substitute(number_substitute_choiced, number_products_choice)

        elif main_choice == "2":
            my_data.display_substitute_saved()

        elif main_choice == "3":
            self.create_tables_open_food_fact()

        elif main_choice == "4":
            sys.exit(0)

    def init_program(self):
        self.get_products_key_from_api()
        self.display_data_open_food_fact()


if __name__ == "__main__":
    m = Main()










