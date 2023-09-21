
def sum_of_digits(n):
    
    if n < 10:
        return n
    
    else:
        
        return n % 10 + sum_of_digits(n // 10)

user_Value =input("Enter a number:")

try:
    number = int(user_Value)
    result =sum_of_digits(number)
    print("Sum of Digits:",result)

except ValueError:

    print("Invalid input !! , Please enter a valid number..")        


