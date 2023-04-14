class Cash_register:

    def main(self):
        self.run = True
        self.run_time = 1
        while self.run == True:
            self.Get_input()
            self.Process_inputs()
            self.Do_calculations()
            self.Pay()
            self.Query()
            self.run_time += 1

    def Get_input(self):
        print()
        print()
        print("Thank you for using Josh print registers!")
        print(f"This is order number {self.run_time}")
        print()


        if self.run_time < 2:
            self.price_child = float(input("What is the price of a child's meal?  "))
            self.price_adult = float(input("What is the price of an adult's meal?  " ))
            self.tax_rate = float(input("What is the sales tax rate?  "))
        else:
            print(f"Adult meal price is ${self.price_adult}")
            print(f"Child meal price is ${self.price_child}")
            print(f"The sales tax rate is set to {self.tax_rate*100}%")
            print()
        self.quantity_child = float(input("How many children are there?  "))
        self.quantity_adult = float(input("How many adults are there?  "))
        
    def Process_inputs(self):
        if self.tax_rate > 1:
            self.tax_rate = self.tax_rate / 100

    def Do_calculations(self):
        self.subtotal = round((self.price_adult*self.quantity_adult)+(self.price_child*self.quantity_child),2)
        print(f"Subtotal: ${self.subtotal}")
        self.Sales_tax = round((self.subtotal*self.tax_rate),2)
        print(f"Sales Tax: ${self.Sales_tax}")
        self.Total = round((self.Sales_tax + self.subtotal), 2)
        print(f"Total: ${self.Total}")

    def Pay(self):
        pay = 0
        while pay <= self.Total:
            pay += float(input("What is the payment amount?  $"))
            if (self.Total - pay) <= 0:
                print(f"Change: {round((abs(self.Total - pay)),2)}")
                print("Have a nice Day!!")
                print()
                return()
            else:
                print(f"Remaining charge: {round((self.Total - pay),2)}")

    def Query(self):
        self.run = input("run again? (y/n)   ") == 'y'
        if self.run:
            reset = input("would you like to adjust prices or taxrate? (y/n)   ")
            if reset == 'y':
                self.run_time = 1
        print()
        print()
        print()

cash = Cash_register()
cash.main()