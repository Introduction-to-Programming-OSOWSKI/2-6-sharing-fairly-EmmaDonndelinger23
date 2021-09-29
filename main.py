#WRITE YOUR CODE IN THIS FILE
def shareFair(x, y):
    if x % y == 0:
        return True
    else:
        return False
print(shareFair(10, 2))
print(shareFair(3, 11))