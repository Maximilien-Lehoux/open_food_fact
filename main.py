import sys

from api_data import DataApi
from constants import URL_GENERAL, LIST_GENERAL
from menu import Menu
from configuration import CATEGORIES
from tables_mysql import CreateDataBase
from display_data import DisplayData


class Main:

    def __init__(self):
        self.init_program()

    def get_products_key_from_api_test(self):
        i = 0
        while i < 5:
            products_json = DataApi("{}{}".format(URL_GENERAL, CATEGORIES[i]))
            self.products = \
                products_json.select_key_test(products_json.data['products'],
                                              'product_name_fr',
                                              'generic_name_fr', 'url',
                                              'stores', 'nutrition_grade_fr',
                                              (i + 1), LIST_GENERAL)
            i += 1

    def create_tables_open_food_fact(self):
        """Tables are created"""
        self.my_tables = CreateDataBase()
        self.my_tables.create_tables()

    def insert_data_tables_mysql(self):
        self.my_tables.insert_categories()
        self.my_tables.insert_products(self.products)

    def display_data_open_food_fact(self):
        """data is displayed in the console"""
        # instantiate menu and database data
        my_menu = Menu()
        self.display_data = DisplayData()

        # main menu is displayed
        main_choice = my_menu.main_menu()

        # the user chooses "1"
        if main_choice == "1":

            # the 5 categories are displayed
            self.display_data.display_categories()

            # category products displayed
            category_choice = my_menu.menu_category()
            self.display_data.display_products_from_category(category_choice)

            # the substitutes for the chosen product are displayed
            number_products_choice = my_menu.menu_products(
                int(category_choice))
            self.display_data.display_substitutes(category_choice)

            # the user chooses a substitute and saves it in the database
            number_substitute_choiced = my_menu.menu_choice_substitute(
                int(category_choice))
            self.display_data.saved_substitute(number_substitute_choiced,
                                     number_products_choice)

        # the user chooses "2" to see his registered substitutes
        elif main_choice == "2":
            self.display_data.display_substitutes_saved()

        # the user chooses "3" to reset the database
        elif main_choice == "3":
            self.get_products_key_from_api_test()
            self.create_tables_open_food_fact()
            self.insert_data_tables_mysql()

        # the user chooses "4" to exit the program
        elif main_choice == "4":
            sys.exit(0)

    def init_program(self):
        self.display_data_open_food_fact()


if __name__ == "__main__":
    m = Main()

