# importing required modules
# import port module
import addition
# importing function
from subtraction import sub

#importing module with alias name
import multiplication as MUL
# importing function with alias name
from division import div as DIV

if __name__ == "__main__":
    print("Welcome to small calculator")
    while True:
        print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division\n 5. exist")
        choice = int(input())
        if choice == 1:
            a, b = map(int, input("Enter two number with seperated by space:").split())
            res = addition.add(x=a, y=b)
            print(f"Addition of {a} and {b} is: {res}")
        elif choice == 2:
            a, b = map(int, input("Enter two number with seperated by space:").split())
            res = sub(x=a, y=b)
            print(f"Subtraction of {a} and {b} is: {res}")
        elif choice == 3:
            a, b = map(int, input("Enter two number with seperated by space:").split())
            res = MUL.mul(x=a, y=b)
            print(f"Multiplication of {a} and {b} is: {res}")
        elif choice == 4:
            a, b = map(int, input("Enter two number with seperated by space:").split())
            res = DIV(x=a, y=b)
            print(f"Division of {a} and {b} is: {res}")
        elif choice == 5:
            print("Thank for using this small calculator app")
            exit()
        else:
            print("Invalid choice")