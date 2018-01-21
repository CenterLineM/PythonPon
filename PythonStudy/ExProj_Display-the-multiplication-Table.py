# Python program to find the multipication tabel (from 1 to 10) of a number input by the user

# take input from the user
num = int(input("Display multiplication table of? "))

#use for loop to iterate 1 times
for i in range(1,11):
    print(num,'x',i,'=',num*i)
