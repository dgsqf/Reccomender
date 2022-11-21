class User:
    """class for a user and is preferences"""
    def __init__(self,name:str,ratings:dict) -> None:
        self.name=name
        self.ratings=ratings
