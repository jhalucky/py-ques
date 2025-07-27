import math

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to find the next prime number after n
def next_prime(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# Main block
if __name__ == "__main__":
    # Take input from user
    n = int(input("Enter a number: "))
    # Find and print the next prime
    print("Next prime number is:", next_prime(n))
