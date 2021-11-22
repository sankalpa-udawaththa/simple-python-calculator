print("select an operation to perform")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")



operation = input()

if operation == "1":
    num1 = input("enter first num:   ")
    num2 = input("enter second num:   ")
    print("the sum is " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("enter first num:   ")
    num2 = input("enter second num:   ")
    print("the difference is " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("enter first num:   ")
    num2 = input("enter second num:   ")
    print("the product is " + str(int(num1) * int(num2)))

elif operation == "4":
    num1 = input("enter first num:   ")
    num2 = input("enter second num:   ")
    print("the result is " + str(int(num1) / int(num2)))

else:
    print("invalid entry")
