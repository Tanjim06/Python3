#factorial

# n! = 1 * 2 * 3 * 4 * 5 *......*n
# n! = [1 * 2 * 3 * 4 * 5 *......* n-1] * n
# n! = n * (n-1)!


# 5! = 1 * 2 * 3 * 4 * 5
# 4! = 1 * 2 * 3 * 4 
# 3! = 1 * 2 * 3 
# 2! = 1 * 2 
# 1! = 1 

# n = 5
# product = 1

# for i in range(n):
#     product = product*(i+1)
    
# print(product)    



# def factorial_iter(n):
#     product = 1

#     for i in range(n):
#         product = product*(i+1)
#     return product 

# print(factorial_iter(5))    


def factorial_recur(n):

    if n==1 or n==0:
        return 1
    
    return n * factorial_recur(n-1)

print(factorial_recur(5))

