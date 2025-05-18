from pages.api.BaseAPI import BaseApi
from utils.utils import api_yml_reader

class Sample(BaseApi):

    def __init__(self):
       super().__init__()
       self.yml =  api_yml_reader('sample.yml')

    def get_users(self):
        endpoint = self.yml['get_users']['endpoint']
        response = self.get(endpoint)
        return response.status_code,response.json()