string1 = 'Welcome to myplace'  
print(type(string1))  

string2 = b'Welcome to myplace'  
print(type(string2)) 



byteData = b"Lets eat a \xf0\x9f\x8d\x95!"  
  
print(type(byteData)) 

str1 = byteData.decode('UTF-8')  
print(type(str1))  
print(str1)
