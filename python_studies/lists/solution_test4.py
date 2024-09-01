def solution(n):
    reverse_n = 0
    
    while n>0:
        digit = n % 10
        reverse_n *= 10
        reverse_n += digit
        n = n // 10
    
    return(reverse_n)


n = 24681
print(solution(n))