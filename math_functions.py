'''library of algorithmic functions
created by Gad and Haim'''

def welcome():
    '''welcome function'''
    print('welcometo the algorithmic functions library!')

if __name__ == '__main__':
    welcome()

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
if __name__ == "__main__":
    print(factorial(100))