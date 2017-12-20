def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            print("not prime")
            break
    else:
        print("The number is prime")

is_prime(12)

