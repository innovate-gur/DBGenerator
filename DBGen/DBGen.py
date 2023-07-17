import json
import os


class DBG(object):
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.type = None
        
    def file(self):
        os.system(f"touch {self.fileName}.json")
        
    def delfile(self):
        os.system(f"rm {self.fileName}.json")
        
    def write(self, content):
        with open(f"{self.fileName}.json", "w") as f:
            json.dump(content, f)

            
    def read(self):
        with open(f"{self.fileName}.json", "r") as f:
            return json.load(f)
            