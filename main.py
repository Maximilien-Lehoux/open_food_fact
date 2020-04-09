import json
import requests
import mysql.connector

from api_data import *


class Main:

    def __init__(self):
        self.init_categories()

    def get_products_from_api(self):
        i = 0
        while i < 5:
            products_category1 = DataApi("{}{}".format(url_general, category[i]))
            print(products_category1.data)
            i += 1

    def init_categories(self):
        self.get_products_from_api()


if __name__ == "__main__":
    m = Main()










