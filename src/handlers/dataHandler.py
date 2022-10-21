import json
import requests

class DataAPI:
    def __init__(self, entries = json.loads(requests.get("https://jsonplaceholder.typicode.com/users").text)):
        self.entries = entries
        self.websites = {}
        self.users = {}
        
    @property
    def list_users_websites(self):
        list_of_websites = []
        for entry in self.entries:
            website = {
                'website' : entry["website"]
            }
            list_of_websites.append(website)   
        self.websites['websites'] = list_of_websites
        return json.dumps(self.websites)
    
    @property
    def list_users_name_email_company(self):
        list_of_users = []
        for entry in self.entries:
            user = {
                "name": entry["name"],
                "email": entry["email"],
                "company": entry["company"]["name"]
            }
            list_of_users.append(user)
        self.users['users'] = list_of_users
        return json.dumps(self.users)
    
    def list_users_by_query(self, incompleteName):
        list_of_users = []
        filteredUsers = [entry for entry in (self.entries) if (incompleteName).lower() in (entry['name']).lower()]
        for filteredUser in filteredUsers:
            user = {
                "id": filteredUser["id"],
                "name": filteredUser["name"],
            }
            list_of_users.append(user)
        self.users['users'] = sorted(list_of_users, key=lambda x: x['name'], reverse=False)
        return json.dumps(self.users)
    
    
    
#Usado somente para teste das properties e methods    
if(__name__ == "__main__"):
    teste = DataAPI()
    print(teste.list_users_by_query('cle'))
                