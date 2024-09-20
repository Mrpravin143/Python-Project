a =eval(input("Enetr the first Number:--"))
b =eval(input("Enter the second Number:--"))
opr=input("Enter thr opr(+,-,*,/):--")
if opr=='+':
    print("Additon is:--",a+b)
elif opr=='-':
    print("Substraction is:--",a-b)
elif opr=="*":
    print("Multiplication is:--",a*b)
elif opr=="/":
    print("Division is:--",b/a)
else:
    print("Invalid Operator....")