def special_order(inputString):
    result = ''
    str_len = len(inputString)
    
    for i in range(str_len//2 + str_len%2):
        result += inputString[str_len - i -1]
    
    for i in range(str_len//2):
        result += inputString[i]
    
    return(result)


string_in = 'abcdefghijk'
print(special_order(string_in))