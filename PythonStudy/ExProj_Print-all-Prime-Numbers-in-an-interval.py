# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the usr
lower = int(input("Eneter Lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                i = i + 1
                break
            else:
                print(num)
                i = i + 1
