import math
def solution(numbers):
    # TODO: Implement solution here
    sum_list = []
    numbers_length = len(numbers)
    
    for i in range(math.ceil(numbers_length/2)):
        sum_temp = numbers[i] + numbers[(numbers_length-i-1)]
        print(sum_temp)
        sum_list.append(sum_temp)
        
    return(sum_list)


list = [1,2,3,4,5]
print(solution(list))