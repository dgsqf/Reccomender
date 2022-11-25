import Content
import DataStore
import User

import random
import string
import Reccomendation
tags=["adventure","gaming","just chatting","shorts"]
datastore = DataStore.DataStore()
for i in range(1000):
    datastore.add_content(Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=3)))




Reccomendation.Reccomend(User.User("".join(random.choices(string.ascii_letters,k=10)),{Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=3)):random.randint(0,10),Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=3)):random.randint(0,10),Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=3)):random.randint(0,10),Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=3)):random.randint(0,10)}),datastore)
