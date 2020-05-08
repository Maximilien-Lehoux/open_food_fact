import sys

from api_data import DataApi
from constants import URL_GENERAL, LIST_GENERAL
from menu import Menu
from configuration import CATEGORIES
from tables_mysql import CreateDataBase
from display_data import DisplayData


class Main:

    def __init__(self):
        self.my_tables = CreateDataBase()
        self.my_menu = Menu()
        self.display_data = DisplayData()
        self.init_program()

    def get_products_key(self):
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
        return self.products

    def create_tables_open_food_fact(self):
        """Tables are created"""
        self.my_tables.create_tables()

    def insert_data_tables_mysql(self):
        self.my_tables.insert_categories()
        self.my_tables.insert_products(self.products)

    def display_data_open_food_fact(self):
        """data is displayed in the console"""
        # main menu is displayed
        main_choice = self.my_menu.main_menu()

        # the user chooses "1"
        if main_choice == "1":
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

        # the user chooses "2" to see his registered substitutes
        elif main_choice == "2":
            self.display_data.display_substitutes_saved()
        # the user chooses "3" to reset the database
        elif main_choice == "3":
            self.create_tables_open_food_fact()
            self.insert_data_tables_mysql()
        # the user chooses "4" to exit the program
        elif main_choice == "4":
            sys.exit(0)

    def display_categories_test(self):
        self.display_data.display_categories()

    def display_products_by_category_test(self):
        self.category_choice = self.my_menu.menu_category()
        self.display_data.display_products_from_category(self.category_choice)

    def display_substitutes_by_products_test(self):
        self.number_products_choice = self.my_menu.menu_products(
            len(self.products))
        self.display_data.display_substitutes(self.category_choice)

    def saved_substitutes_test(self):
        number_substitute_choiced = self.my_menu.menu_choice_substitute(
            len(self.products))
        self.display_data.saved_substitute(number_substitute_choiced,
                                           self.number_products_choice)

    def display_substitutes_choice_test(self):
        self.display_data.display_substitutes_saved()

    def reset_database_test(self):
        self.create_tables_open_food_fact()
        self.insert_data_tables_mysql()

    def quit_program_test(self):
        sys.exit(0)

    # def navigate_menu(self):
        # main_choice = self.my_menu.main_menu()
        # if main_choice == 1:
            # self.display_categories_test()
            # self.display_products_by_category_test()
            # self.display_substitutes_by_products_test()
            # self.saved_substitutes_test()
        # elif main_choice == 2:
            # self.display_substitutes_choice_test()
        # elif main_choice == 3:
            # self.reset_database_test()
        # elif main_choice == 4:
            # self.quit_program_test()

    def init_program(self):
        self.get_products_key()
        self.display_data_open_food_fact()


if __name__ == "__main__":
    m = Main()
