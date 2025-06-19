'''library of algorithmic functions
created by Gad and Haim'''

def welcome():
    '''welcome function'''
    print('welcometo the algorithmic functions library!')

def is_prime(n, i = 2):
    if n < 2:
        return False 
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    welcome()
    print(factorial(100))

