def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
try:
   number = int (input("Enter the number:"))

   if number < 0:
       
       print("Factorial is not defined for negative numbers...")

   else:
       result = factorial(number)
       print(f"Factorial of {number} is :",result)

except ValueError:
    print("Invalid input value !! , Please enter a valid number.")