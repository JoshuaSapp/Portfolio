

class Cart:

    def __init__(self):
        self.cart_items = []
        self.price_index = {}

    def add_item_to_price_index(self,item):
        print()
        print()
        
        print(f"--- Please declare price for {item} ---")
        price = float(input("Item price:  "))
        print()
        print(f"-- Add {item} with price ${price}?  (y/n) --")
        confirm = input("Confirm: ")
        confirm = confirm.lower()
        if confirm != 'y':
            print()
            print("-- Ok, lets try again --")
            self.add_item_to_price_index(item)
        else:
            self.price_index.update({item:price})

    def add_item_to_cart(self,item,count):
        if item not in self.price_index:
            print()
            print("--- New item detected ---")
            print()
            self.add_item_to_price_index(item)
        while count > 0:
            self.cart_items.append(item)
            count -= 1

    def remove_item_from_cart(self,item,count):
        item_count = {}
        for item in self.cart_items:
            if item not in item_count:
                item_count.update({item:1})
            else:
                item_count[item] += 1
        if item_count[item] <= count:
            count = item_count[item]
            while count > 0:
                self.cart_items.remove(item)
                count -= 1
            return(item_count[item])
        else:
            while count > 0:
                self.cart_items.remove(item)
                count -= 1
            return(count)            



    def check_cart(self):
        item_counts = {}
        item_values = {}
        
        for item in self.cart_items:
            value = self.price_index[item]
            if item not in item_counts:
                item_counts.update({item:1})
            if item not in item_values:
                item_values.update({item:value})
            else:
                item_counts[item] += 1
                value = value + float(item_values[item])
                item_values[item] = value

        print()
        print()
        print("--- Cart ---")
        print("--- Item --- Count --- Value ---")
        total = [0,0]
        for item in item_counts:
            print(f"--- {item} --- {item_counts[item]} --- ${item_values[item]} ---")
            total[0] += item_counts[item]
            total[1] += item_values[item]
        print(f"--- Totals --- {total[0]} --- ${total[1]} ---")
        print()
        print("-- end cart --")

    def check_prices(self):
        print()
        print()
        print("--- Prices ---")
        for item in self.price_index:
            print(f"{item}: ${self.price_index[item]}")

class gui:

    def __init__(self):
        self.cart = Cart()

    def start(self):
        print()
        print("Welcome to Josh-cart!  Have fun shopping!")
        print()
        self.mainMenu()

    def mainMenu(self):
        print()
        print("Main Menu")
        print("1.Add item to cart")
        print("2.Remove item from cart")
        print("3.Check Prices")
        print("4.Check Cart")
        print("5.Quit")
        choice = int(input("Choice:  "))
        if choice == 1:
            self.add_item_menu()
        if choice == 2:
            self.remove_item_menu()
        if choice == 3:
            self.cart.check_prices()
            self.mainMenu()
        if choice == 4:
            self.cart.check_cart()
            self.mainMenu()
        if choice == 5:
            print()
            print("--- Thanks for using Josh-cart! ---")

    def add_item_menu(self):
        print()
        print()
        print("--- Adding item to cart ---")
        print("--- What item would you like to add? ---")
        item = str(input("New item:  "))
        print()
        print("--- How many would you like to add? ---")
        add = int(input("Item count:   "))
        self.cart.add_item_to_cart(item,add)
        print()
        print("--- Item added successfully! ---")
        self.mainMenu()


    def remove_item_menu(self):
        print()
        print()
        print("--- Removing item to cart ---")
        print("--- What item would you like to remove? ---")
        item = str(input("remove item:  "))
        print()
        print("--- How many would you like to remove? ---")
        count = int(input("Item count:   "))
        result = self.cart.remove_item_from_cart(item,count)
        if result == 0:
            print("--- Items removed successfully!")
            self.mainMenu()
        else:
            print(f"--- Removed {result} {item} from cart. ---")
            print(f"--- There are no more {item} in the cart ---")
            self.mainMenu()            


main = gui()
main.start()