#Write a Python program to print the multiplication table of a given number. The user should be able to input the number for
# which they want the multiplication table, and the program should display the table up to user-defined range
start=int(input('Enter the start value : '))
stop=int(input('Enter the stop value : '))
num=int(input('Enter the number : '))
for i in range(start,stop+1):
    value=i*num
    print(num,'x',i,'=',value)











