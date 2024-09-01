import math
def solution(numbers):
    # TODO: implement this function
    x = len(numbers)
    output = []
    
    for i in range(x):
        output.append((numbers[i],round((math.sqrt(numbers[i]*(numbers[(x-i-1)]))),2)))
    return(output)


list = [1,2,3,4,5]
print(solution(list))