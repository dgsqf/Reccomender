import Content
import DataStore
import User

datastore = DataStore.DataStore()

datastore.add_content(Content.Content("Hello World",["programming","begginer"]))
datastore.add_user(User.User("name",{Content.Content("Hello World",["programming","begginer"]):10}))
datastore.store()