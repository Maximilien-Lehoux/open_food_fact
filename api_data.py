import json
import requests

from configuration import *
from constant import *

# the parameters when calling the API. the categories can be modified
# in the configuration.py file as well as the number of products by category
payload_products = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': CATEGORIES,
    'tagtype_1': 'nutrition_grade',
    'tag_contains_1': 'contains',
    'fields': ','.join(API_TO_PRODUCT_FIELDS.keys()),
    'page_size': NUMBER_PRODUCTS,
    'json': 'true',
}

class DataApi:
    """the request to the API which contains the parameters"""
    def __init__(self, url):
        self.response = requests.get(url, params=payload_products)
        self.data = self.response.json()

    def select_key(self, data, key, selected_list):
        """The different keys are sorted and placed in lists"""
        # selected_list = []
        for item in data:
            selected_list.append(item.get(key))
        return selected_list