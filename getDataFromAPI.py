import requests

class DataHandler:
    def __init__(self):
        self.text = requests.get("https://jsonplaceholder.typicode.com/users").text
    
    def GetData(self):
        return self.text