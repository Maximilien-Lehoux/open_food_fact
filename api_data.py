import json
import requests

payload = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': category,
    'tagtype_1': 'nutrition_grade',
    'tag_contains_1': 'contains',
    'fields': ','.join(API_TO_PRODUCT_FIELDS.keys()),
    'page_size': nb,
    'json': 'true',
}

class DataApi:
    def __init__(self, url):
        self.response = requests.get(url)
        self.data = self.response.json()

    def upload_json_file(self, file_json, data):
        with open(file_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)