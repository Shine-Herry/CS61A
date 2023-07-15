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

def fizzbuzz(n):
    if n > 0:
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                print('fizzbuzz')
            elif i % 3 == 0:
                print('fizz')
            elif i % 5 == 0:
                print('buzz')
            else:
                print(i)
            i += 1
    else:
        return True
    
def unique_digits(n):
    i , k = 0, 0 
    while i <= 9:    
        if has_digit(n, i) :
            k += 1
        i += 1
    return k
        

def has_digit(n, k):
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False

unique_digits(465460)