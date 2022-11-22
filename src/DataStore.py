class DataStore:
    def __init__(self) -> None:
        self.content = []
        self.users= []
    
    def store(self):
        data={
            "content":[i.to_json() for i in self.content],
            "users":[j.to_json() for j in self.users]

        }
        print(data)
    def add_content(self,content):
        self.content.append(content)
    def add_user(self,user):
        self.users.append(user)