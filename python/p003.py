# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#list to store divisible numbers
divisible = []

# iterator
i = 2

# while loop to see if number is divisible
while i < 13195:
    if 13195 % i == 0:
        divisible.append(i)
        print(i)
        i += 1

# function to check if number is prime
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else: return True