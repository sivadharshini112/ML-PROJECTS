'''def welcome(name):
    return("welcome",name)
print(welcome("shivani"))'''



'''def square(num1,num2):
    return(num1**num2)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(square(a,b))'''


'''
def area_circle(radius):
    area=3.14*radius*radius
    return area
r=int(input("Enter the number:"))
result=area_cricle(r)
print("Area of Circle=",result)'''



def withdraw(balance, amount):
    if amount % 100 != 0:
        return "Amount should be a multiple of 100"

    elif amount > balance:
        return "Insufficient balance"
    else:
     balance -= amount
     return f"Withdrawal successful. Remaining balance: {balance}"
a=int(input("enter the balance:"))
b=int(input("enter the amount:"))
print(withdraw(a,b))

