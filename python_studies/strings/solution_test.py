def reversed_triple_chars(s: str) -> str:
    str_len = len(s)
    
    counter = int((str_len)/3)
    leftover_counter = int((str_len)%3)

    
    result = ''

    for i in range(counter):
        #print(i)
        #print(temp_counter)

        temp_str = ''
        reverse_str_temp = ''

        for j in range(3):
            temp_counter = (((i) * 3) + j)
            temp_str += (s[temp_counter])

        print(temp_str)
        
        for k in range(3):
            temp_run = ((3 * i) + 2) - k
            print(temp_run)
            reverse_str_temp += (s[temp_run])
        print(reverse_str_temp)

        result += reverse_str_temp

    for l in range(leftover_counter):
        result += (s[counter*3 + l])
 
    return(result)


string_in = 'abcdefgh'
print(reversed_triple_chars(string_in))