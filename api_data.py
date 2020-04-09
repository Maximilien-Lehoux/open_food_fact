import json
import requests

from configuration import *
from constant import *

payload = {
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


class DataApi:
    def __init__(self, url):
        self.response = requests.get(url, params=payload)
        self.data = self.response.json()
