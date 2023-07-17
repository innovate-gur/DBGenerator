import json
import os


class DBG(object):
    def __init__(self, fileName):
        self.fileName = fileName
        
    def file(self):
        os.system(f"touch {self.fileName}.json")
        
    def delfile(self):
        os.system(f"rm {self.fileName}.json")
        
    def write(self, content):
        with open(f"{self.fileName}.json", "w") as f:
            json.dump(content, f)
        
            