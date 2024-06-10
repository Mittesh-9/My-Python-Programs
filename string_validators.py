def string_validation(string):
    if any(char.isalnum() for char in string):          #0 qA2 #1 123 >> EO >> TFTFF
        print ("True")
    else:
        print ("False")
    
    if any(char.isalpha() for char in string):
        print ("True")
    else:
        print ("False")
    
    if any(char.isdigit() for char in string):
        print ("True")
    else:
        print ("False")
    
    if any(char.islower() for char in string):
        print ("True")
    else:
        print ("False")
    
    if any(char.isupper() for char in string):
        print ("True")
    else:
        print ("False")
        
string_validation("123")

# True
# False
# True
# False
# False