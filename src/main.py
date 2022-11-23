import Content
import DataStore
import User

datastore = DataStore.DataStore()
for i in range(100000):
    datastore.add_content(Content.Content("Hello World",["programming","begginer"]))

    datastore.add_user(User.User("name",{Content.Content("Hello World",["programming","begginer"]):10}))


data=datastore.store()

datastore2=DataStore.DataStore()
datastore2.load(data)


print(datastore.store()==datastore2.store())