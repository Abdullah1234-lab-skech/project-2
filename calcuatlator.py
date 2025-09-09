def add(P , Q):
    return P + Q 
def subtract(P , Q): 
    return P - Q 
def multiply(P , Q):
    return P * Q 
def divide(P , Q):
    return P / Q 
print("Please select an operation") 
print("1.Add") 
print("2.Subtract") 
print("3.Multiply") 
print("4.Division") 
choice=input("Enter choice 1/2/3/4:") 
number1=int(input("Enter the first number:")) 
number2=int(input("Enter the second number:")) 
if choice=='1':
    print(number1,'+',number2,'=',add(number1,number2))
elif choice=='2':
    print(number1,'-',number2,'=',subtract(number1,number2)) 
elif choice=='3':
    print(number1,'*',number2,'=',multiply(number1,number2)) 
elif choice=='4': 
    print(number1,'/',number2,'=',divide(number1,number2)) 
else:
    print("Invailid input")