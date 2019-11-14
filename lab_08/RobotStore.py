
# Class for Products
class Product:

    # Constructer Function
    def __init__(self, name, cost, stock):
        self.name = name
        self.cost = cost
        self.stock = stock
        self.totalCost = 0
    
    # Method for checking if in stock
    def ifInStock(self, amount):
        if(self.stock >= amount ):
            print("There is", amount, "of", self.name)
        else:
            print("There is not", amount, "of", self.name, "left in stock")
    
    # Method for calculation total cost
    def calcTotalCost(self, count):
        self.totalCost = self.cost * count
    
    # Method for buying product
    def buyProduct(self, purchaseAmount):
        self.stock = self.stock - purchaseAmount
        return self.stock


#List of Class
productList = []

# Adding to the List
productList.append(Product("Ultrasonic range finder", 2.50, 4))
productList.append(Product("Servot Motor", 14.99, 10))
productList.append(Product("Servo Controller", 44.95, 5))
productList.append(Product("Microcontroller Board", 34.95, 7))
productList.append(Product("Laser Range Finder", 149.99, 2))
productList.append(Product("Lithium Polymer Battery", 8.99, 8))



def print_stock():
    print("\nAvailable Products")
    print("-------------------")
    for i in range(0, len(productList)):
        if productList[i].stock > 0:
            print(str(i) + ')' , productList[i].name, "$" , productList[i].cost, ". We have", productList[i].stock, "in Stock")
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])
        productList[prod_id].calcTotalCost(count)

        if productList[prod_id].stock >= count:
            if cash >= productList[prod_id].totalCost:
                cash = cash - productList[prod_id].totalCost
                productList[prod_id].stock - count
                print("You purchased", count, "of", productList[prod_id].name  + '.')
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product")
        else:
            print("Sorry, we are sold out of", productList[prod_id])


main()
