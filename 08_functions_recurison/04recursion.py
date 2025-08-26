'''

0! = 1
1! = 1
2! = 2 x 1
3! = 3 x 2 x 1
4! = 4 x 3 x 2 x 1
5! = 5 x 4 x 3 x 2 x 1

n! = n x n-1 x......3 x 2 x 1
n! = n * factorial(n-1)

'''


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"the factorial of this number is: {factorial(n)}")