import DBGen.DBGen as dbg

# make your own main.py file

if __name__ == "__main__":
    
    C = dbg.DBG("data")
    
    C.file()
    C.write([124, 1245, 'ho'])
    print(list(C.read())[2])