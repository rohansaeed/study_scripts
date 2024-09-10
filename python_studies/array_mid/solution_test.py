def solution(numbers):
    half_len = len(numbers)//2
    result = []
    left_num = 0
    right_num = 0

    if len(numbers)>0 and len(numbers) % 2 == 1:
        result.append(numbers[half_len])
        left_num = half_len -1
        #print(left_num)
        right_num = half_len + 1
        #print(right_num)
    else:
        left_num = half_len -1
        #print(numbers[left_num])
        right_num = half_len
        #print(numbers[right_num])

    while left_num >= 0:
        print(numbers[left_num])
        print(numbers[right_num])
        result.append((numbers[left_num])*(numbers[right_num]))

        left_num -= 1
        right_num += 1
    
    return(result)


array_in = [5, -7, 2, -9, 1, -3, 8]
print(solution(array_in))