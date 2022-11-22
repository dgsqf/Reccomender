class Content:
    """
    Class for a piece of content (movie,music,image...)
    """
    def __init__(self,name:str,tags:list) -> None:
        self.name=name
        self.tags=tags
    def to_json(self):
        """return the object in a json format"""
        data={self.name:self.tags}
        return f"{data}"
    

    
