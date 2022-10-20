import json
import requests

class Data:
    def __init__(self):
        self.entries = json.loads(requests.get("https://jsonplaceholder.typicode.com/users").text)
        self.websites = []
        self.users = []
        
    @property 
    def list_websites(self):
        for entry in self.entries:
            self.websites.append({entry["website"]})
        return self.websites
    
    @property
    def list_name_email_company(self):
        for entry in self.entries:
            self.users.append({"name": entry["name"], "email": entry["email"], "company": entry["company"]["name"]})
        return self.users
    
    def list_user_by_query(self, incompleteName):
        filteredUsers = [entry for entry in (self.entries) if (incompleteName).lower() in (entry['name']).lower()]

        for filteredUser in filteredUsers:
            self.users.append({"id": filteredUser["id"],"name": filteredUser["name"]})
        
        return sorted(self.users,key=lambda x: x['name'], reverse=False)
                