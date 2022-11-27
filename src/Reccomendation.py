import User
import DataStore
import numpy as np
def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm
def Reccomend(user:User,DataStore:DataStore):
    content=DataStore.content
    tags=set()
    for i in content:
        for t in i.tags:
            tags.add(t)
    tags=sorted(list(tags))

    user_profile=np.zeros(len(tags))
    for i in user.ratings.items():
        user_profile=np.add(get_movie_vector(tags,i[0])*i[1],user_profile)
    user_profile= normalize(user_profile)
    print(user_profile)

def get_content_vector(tags,content):
    vector=np.zeros(len(tags))
    
    for i,x in enumerate(tags):
        if x in content.tags:
            vector[i]=1
    
    return vector




