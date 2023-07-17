import json
import os


class DBG(object):
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.type = None
        
    def make(self):
        os.system(f"rm {self.fileName}.json") #check if self.fileName is existing
        os.system(f"touch {self.fileName}.json")
        
    def delete(self):
        os.system(f"rm {self.fileName}.json")
        
    def write(self, content):
        with open(f"{self.fileName}.json", "w") as f:
            json.dump(content, f)
        self.type = type(content)
            
    def add(self, content):
        if self.type is not type(content):
            raise TypeError(f"can't add {type(content)} to {self.type}")
        read = self.read()
        with open(f"{self.fileName}.json", "w") as f:
            json.dump(read + content, f)
    
            
    def read(self):
        with open(f"{self.fileName}.json", "r") as f:
            if self.type is list:
                return list(json.load(f))
            if self.type is str:
                return str(json.load(f))
            if self.type is dict:
                return dict(json.load(f))
            else:
                raise TypeError("Type 'int' not supported")
            