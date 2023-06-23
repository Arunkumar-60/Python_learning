# sum_of_digits
n=int(input())
def sum_of_digits(n):
    sum=0
    while n>0:
        sum=sum+(n%10)
        sum_of_digits(n//10)
    return sum
print("the sum of digits og the number",n,"is",sum_of_digits(n))
