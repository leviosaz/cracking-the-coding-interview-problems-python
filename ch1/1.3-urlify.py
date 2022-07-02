def URLify(string):
    new_string = ""
    
    for x in string:
        if x == " ":
            new_string += "%20"
            continue
        new_string += x 
    
    return new_string
    
    
print(URLify("john doe is something"))