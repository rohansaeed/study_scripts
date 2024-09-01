def solution(n):
    result = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        # Place two identical digits in their correct places
        result += digit * multiplier
        multiplier *= 10
        result += digit * multiplier
        multiplier *= 10

        n = n // 10

    return(result)


number = 14235
print(solution(number))