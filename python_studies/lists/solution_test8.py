def repeat_char_jump(inputString, k):
    result = ''
    counter = 0
    str_len = len(inputString)

    for i in range(str_len):
        result += inputString[counter]
        counter = ((counter+k)%str_len)

    
    return(result)


string_in = 'abcdefghijk'
jump = 3
print(repeat_char_jump(string_in, jump))