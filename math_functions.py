'''library of algorithmic functions
created by Gad and Haim'''

def welcome():
    '''welcome function'''
    print('welcometo the algorithmic functions library!')

if __name__ == '__main__':
    welcome()
<<<<<<< HEAD
    
def is_prime(n, i = 2):
    if n < 2:
        return False 
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
    

    
=======

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
if __name__ == "__main__":
    print(factorial(100))
>>>>>>> 4625c997d527e1548c23c191ede6d6eafbb35584
