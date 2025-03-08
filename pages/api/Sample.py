import requests
from utils.utils import yml_reader


class Sample:

    def __init__(self):
       self.yml =  yml_reader('sample.yml')

    def get_users(self):
        url = "https://reqres.in/api"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


Sample().get_users()