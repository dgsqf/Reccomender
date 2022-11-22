class User:
    """class for a user and is preferences"""
    def __init__(self,name:str,ratings:dict) -> None:
        self.name=name
        self.ratings=ratings
    def to_json(self):
        return {"name":self.name,
                "reviews":{k.to_json():v for k,v in self.ratings.items()}}