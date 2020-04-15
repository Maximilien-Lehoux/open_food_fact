import json
import requests

from configuration import *
from constant import *

payload_products = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': category,
    'tagtype_1': 'nutrition_grade',
    'tag_contains_1': 'contains',
    'fields': ','.join(API_TO_PRODUCT_FIELDS.keys()),
    'page_size': number_products,
    'json': 'true',
}

temporary_list_product_name = []
temporary_list_generic_name = []
temporary_list_brands = []
temporary_list_url = []
temporary_list_stores = []
temporary_list_nutrition = []


class DataApi:
    def __init__(self, url):
        self.response = requests.get(url, params=payload_products)
        self.data = self.response.json()

    def select_key(self, data, key, selected_list):
        # selected_list = []
        for item in data:
            selected_list.append(item.get(key))
        return selected_list