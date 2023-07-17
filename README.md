<h1 style="text-align: center;">DBGenerator</h1>

<center>to generate simple database easily</center>

## installation

```console 
git clone https://github.com/Juhyun-KK/DBGenerator
```




## Document
```python
import DBGen.DBGen as dbg


C = dbg.DBG("data") #name file
    
C.make() #create file data.json

C.write([1, 2, 'three']) #write over file
print(C.read()) #returns file content

C.write("Hello, I'm a data") 
print(C.read())

C.add("\n Hello, I'm added data") #add data without overwriting file
print(C.read())

C.delete() #delete file


```