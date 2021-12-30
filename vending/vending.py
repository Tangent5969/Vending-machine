import os.path
balance = float(0)

def set_balance():
    newBalance = open("balance.txt", 'w')
    newBalance.write(str(balance))
    newBalance.close()

def get_balance():
    currentBalance = open("balance.txt", 'r')
    balance = round(float(currentBalance.read()), 2)
    currentBalance.close()
    return balance

class item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def dispense(self):
        global balance
        if balance >= self.price and self.stock > 0:
            self.stock -= 1
            balance -= self.price
            set_balance()
            print(f"purchase successful\nyour new balance is: £{balance}\nenjoy your {self.name}!\n")

        elif self.stock == 0: print("this product is unavailable to purchase")
        else:
            print("You have insufficient funds to purchase this product")


itemList = [
    item("Sam", 0.99, 5),
    item("pencil", 6.90, 10),
    item("mouse", 10.00, 2),
    item("chocolate", 1.99, 15),
    item("bomb", 0.99, 1)
]
if os.path.exists("balance.txt") is False:
    f = open("balance.txt", 'w')
    f.write(str(balance))
    f.close()

balance = get_balance()
while True:
    selected = False
    choice = int(input("Press 1 to input money \nPress 2 to select and buy a product\n"))
    if choice == 1:
        print(f"your current balance is: £{balance}")
        balance += float(input("Enter how much you wish to add\n£"))
        set_balance()
        print(f"your new balance is: £{balance}\n")

    elif choice == 2:
        i = 1
        print(f"your current balance is: £{balance}\n")

        for item in itemList:
            if item.stock > 0:
                print(f"{item.name} costs £{item.price} and is in slot: {i}")
            i += 1

        while selected == False:
            selection = int(input("\nEnter the slot number of the product you wish to purchase\n"))
            if selection > len(itemList or selection <= 0):
                print("Enter a valid slot number")
            else:
                selected = True

        chosen = itemList[selection-1]
        chosen.dispense()
