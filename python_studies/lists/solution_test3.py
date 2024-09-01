def solution(n):
    digit_product = 0
    
    while n>0:
        digit = n % 10
        if digit%2 != 0:
            if digit_product == 0:
                digit_product = 1
            digit_product *= digit
        n = n // 10
    
    return(digit_product)


n = 24681
print(solution(n))