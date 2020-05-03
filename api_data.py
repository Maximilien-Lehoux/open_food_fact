import requests

from configuration import CATEGORIES, NUMBER_PRODUCTS
from constants import API_TO_PRODUCT_FIELDS


class DataApi:
    """the request to the API which contains the parameters"""
    def __init__(self, url):
        self.payload_products = {
                            'action': 'process',
                            'tagtype_0': 'categories',
                            'tag_contains_0': 'contains',
                            'tag_0': CATEGORIES,
                            'tagtype_1': 'nutrition_grade',
                            'tag_contains_1': 'contains',
                            'fields': ','.join(API_TO_PRODUCT_FIELDS.keys()),
                            'page_size': '50',
                            'json': 'true',
                            }
        self.response = requests.get(url, params=self.payload_products)
        self.data = self.response.json()

    def select_key_test(self, data, key1, key2, key3, key4, key5,
                        number_category, list_general):
        """The different keys are sorted and placed in lists"""
        for item in data:
            product_list = [item.get(key1), item.get(key2), item.get(key3),
                            item.get(key4), item.get(key5),
                            str(number_category)]
            if '' not in product_list and None not in product_list:
                list_general.append(product_list)
        return list_general
