import User
import DataStore
import numpy as np
import random
def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm
def Reccomend(user:User,DataStore:DataStore):
    results={}
    content=DataStore.content
    tags=set()
    for i in content:
        for t in i.tags:
            tags.add(t)
    tags=sorted(list(tags))

    user_profile=np.zeros(len(tags))
    for i in user.ratings.items():

        if i[0] in content:
            content.remove(i[0])

        user_profile=np.add(get_content_vector(tags,i[0])*i[1],user_profile)
    user_profile= normalize(user_profile)
    
    for x in content:
        vector=np.sum(get_content_vector(tags,x)*user_profile)
        
        results[x]=vector
    return random.choice(list({i for i in results if results[i]==max(results.values())}))

def get_content_vector(tags,content):
    vector=np.zeros(len(tags))
    
    for i,x in enumerate(tags):
        if x in content.tags:
            vector[i]=1
    
    return vector




