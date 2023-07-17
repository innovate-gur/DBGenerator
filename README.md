<h1 style="text-align: center;">DBGenerator</h1>

generate Database  easily

```python
import DBGen.DBGen as dbg
    

C = dbg.DBG("data") #name file
    
C.file() #create file data.json

C.write([1, 2, 'three']) #write over file
print(list(C.read())[2])

C.write("Hello, I'm a data") 
print(str(C.read()))

C.delfile() #delete file


```