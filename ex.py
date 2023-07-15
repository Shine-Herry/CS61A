def is_prime(n):
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            print('False')
            return False
        i += 1
    print('True')
    return True

is_prime(17)
     