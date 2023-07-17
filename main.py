import DBGen.DBGen as dbg
import os
# make your own main.py file

if __name__ == "__main__":
    C = dbg.DBG("data")
    
    C.make()
    C.write("pre")
    C.add("12")
    print(C.read())
