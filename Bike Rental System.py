class ShopBike():
    def __init__(self,stock):
        self.stock=stock
    def TotalBike(self):
        print("Total Bikes:--",self.stock)
    def RentBike(self,qty):
        if qty<=0:
            print("Enter the positive values and greter than zero:--")

        elif qty>self.stock:
            print("Enter the value less than stock:--")
        else:
            self.stock=self.stock-qty
            print("Total price:--",qty*100)
            print("Total Avilable Stock:--",self.stock)

while True:
    obj1=ShopBike(200)
    userchoice=int(input('''
      
      1 Display Bikes
      2 Rent Bike
      3 Exit...
    '''))
    if userchoice==1:
        obj1.TotalBike()
    elif userchoice==2:
        quantity=int(input("Enter the Quantity:--"))
        obj1.RentBike(quantity)
    else:
        break

