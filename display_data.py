from tables_mysql import *


class DisplayData(CreateDataBase):

    def __init__(self):
        super().__init__()

    def display_categories(self):
        """categories are displayed"""
        results = self.get_categories()
        self.display_db_query_results(results)

    def display_products_from_category(self, category_id):
        results = self.get_products_from_category(category_id)
        self.display_db_query_results(results)

    def display_substitutes(self, category_id):
        results = self.get_substitutes(category_id)
        self.display_db_query_results(results)

    def display_substitutes_saved(self):
        """saved substitutes are displayed"""
        results = self.get_substitutes_saved()
        self.display_db_query_results(results)

    def display_db_query_results(self, results):
        for x in results:
            print(x)