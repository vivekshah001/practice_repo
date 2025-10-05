
# Write a program to print all prime numbers between 1 and 100. 


a=100
n=2


if a%1== 0 and a%a == 0:
    print("1 is not prime")
for i in range(2, a + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')