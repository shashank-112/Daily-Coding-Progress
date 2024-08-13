def sumOfSquers(n):
    if n == 1:
        return 1
    return n*n + sumOfSquers(n-1)

print(sumOfSquers(int(input("enter the number u want : "))))