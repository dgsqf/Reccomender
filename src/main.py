import Content
import DataStore
import User
from typing import List
import random
import string
import Reccomendation

datastore = DataStore.DataStore()



from fastapi import FastAPI

app = FastAPI()


@app.post("/addcontent")
async def add_new_content(title:str,tag:list):
    datastore.add_content(Content.Content(title,tag))
    print(datastore.store())


    return {"status":"accepted"}
@app.post('/deletecontent')
async def remove_content(title:str):
    datastore.delete_content(title)
    print(datastore.store())
    return {"status":"accepted"}
