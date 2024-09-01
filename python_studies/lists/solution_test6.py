def solution(n):
    result = 0

    while n > 0:
        temp_digit1 = n%10
        n = n // 10
        temp_digit2 = n%10
        if temp_digit1 == temp_digit2:
            result += 1

    return(result)


number = 14423355
print(solution(number))