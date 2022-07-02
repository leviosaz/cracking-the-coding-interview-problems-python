def stringCompression(string):
    new_string = ""
    current_letter = string[0]
    current_count = 1
    
    for x in string[1:]:
        if x == current_letter:
            current_count += 1
            continue

        new_string += f"{current_letter}{current_count}"
        current_letter = x
        current_count = 1
    
    new_string += f"{current_letter}{current_count}"
    
    if len(new_string) > len(string):
        return string
    return new_string

print(stringCompression("aabccccccaa"))