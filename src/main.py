import Content
import DataStore
import User

import random
import string
import Reccomendation
tags=["adventure","gaming","just chatting","shorts","movies ","movie ","film ","cinema ","films ","hollywood ","actor ","love ","s ","art ","cinematography ","actress ","netflix ","moviescenes ","music ","filmmaking ","horror ","instagood ","bollywood ","movienight ","instagram ","photography ","comedy ","cinephile ","cine ","tv ","director ","horrormovies ","drama ","filmmaker"]
datastore = DataStore.DataStore()
for i in range(1000):
    datastore.add_content(Content.Content("".join(random.choices(string.ascii_letters,k=10)),random.choices(tags,k=5)))





