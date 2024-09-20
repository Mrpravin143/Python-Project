#interest calculotre
amount =int(input("Enter The Amount:--"))
year =float(input("Enter Number of years:--"))
rate =eval(input("Enter the rate:--"))
si =amount*year*rate/100

print("Montly Interest is:--",si)
print("Yearly Interst:--",si*12)