import sys

from api_data import DataApi
from constants import URL_GENERAL
from menu import Menu
from configuration import CATEGORIES
from tables_mysql import CreateDataBase
from display_data import DisplayData


class Main:

    def __init__(self):
        self.main_choice = ""
        self.my_tables = CreateDataBase()
        self.my_menu = Menu()
        self.display_data = DisplayData()
        self.init_program()

    def get_products_key(self):
        temporary_list = []
        i = 0
        while i < len(CATEGORIES):
            products_json = DataApi("{}{}".format(URL_GENERAL, CATEGORIES[i]))
            self.products = \
                products_json.select_key_test(products_json.data['products'],
                                              'product_name_fr',
                                              'generic_name_fr', 'url',
                                              'stores', 'nutrition_grade_fr',
                                              (i + 1), temporary_list)
            i += 1
        return self.products

    def create_tables_open_food_fact(self):
        """Tables are created"""
        self.my_tables.create_tables()

    def insert_data_tables_mysql(self):
        self.my_tables.insert_categories()
        self.my_tables.insert_products(self.products)

    def display_data_choice1(self):
        """data is displayed in the console"""
        # main menu is displayed
        self.main_choice = self.my_menu.main_menu()
        # the user chooses "1"
        if self.main_choice == "1":
            # the 5 categories are displayed
            self.display_data.display_categories()
            # category products displayed
            category_choice = self.my_menu.menu_category()
            self.display_data.display_products_from_category(category_choice)
            # the substitutes for the chosen product are displayed if exist
            # else program quit
            number_products_choice = self.my_menu.menu_products(
                len(self.products))
            self.display_data.display_substitutes(category_choice)
            # the user chooses a substitute and saves it in the database
            number_substitute_choiced = self.my_menu.menu_choice_substitute(
                len(self.products))
            self.display_data.saved_substitute(number_substitute_choiced,
                                               number_products_choice)

    def display_data_choice2(self):
        # the user chooses "2" to see his registered substitutes
        if self.main_choice == "2":
            self.display_data.display_substitutes_saved()

    def display_data_choice3(self):
        # the user chooses "3" to reset the database
        if self.main_choice == "3":
            self.create_tables_open_food_fact()
            self.insert_data_tables_mysql()

    def display_data_choice4(self):
        # the user chooses "4" to exit the program
        if self.main_choice == "4":
            sys.exit(0)

    def init_program(self):
        self.get_products_key()
        self.display_data_choice1()
        self.display_data_choice2()
        self.display_data_choice3()
        self.display_data_choice4()


if __name__ == "__main__":
    m = Main()
