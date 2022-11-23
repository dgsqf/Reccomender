import json
import Content
import User
class DataStore:
    def __init__(self) -> None:
        self.content = []
        self.users= []
    
    def store(self):
        data={
            "content":[i.to_json() for i in self.content],
            "users":[j.to_json() for j in self.users]

        }
        return data
    def add_content(self,content):
        self.content.append(content)
    def add_user(self,user):
        self.users.append(user)
    def load(self,data):

        
        for i in data['content']:

            
            self.add_content(Content.from_json(json.loads(i.replace("'",'"'))))
        for u in data['users']:

            

            
            self.add_user(User.User(name=u["name"],ratings={Content.from_json(json.loads(c.replace("'",'"'))):r for c,r in u["reviews"].items()}))
