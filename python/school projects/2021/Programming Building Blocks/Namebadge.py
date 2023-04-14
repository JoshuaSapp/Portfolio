
class Namebadge:

    def main(self):
        self.getInput()
        self.printID()


    def getInput(self):
        print("Please input the folowing information")
        print()
        self.first_name = input("First Name:   ")
        self.last_name = input("Last Name:   ")
        self.email_address = input("Email Address:   ")
        self.phone_number = input("Phone Number:   ")
        self.job_title = input("Job Title:   ")
        self.id_number = input("ID number:   ")
        self.hair_color = input("Hair Color:   ")
        self.eye_color = input("Eye Color:   ")
        self.Training = input("Training (yes/no):   ")
        self.Month = input("Month:   ")


    def printID(self):
        print()
        print()
        print("-----------------------------")
        print(f"{self.last_name}, {self.first_name}")
        print(f"{self.job_title}")
        print(f"ID: {self.id_number}")
        print()
        print(self.email_address)
        print(self.phone_number)
        print()
        print("Hair: {0:20} Eyes: {1}".format(self.hair_color,self.eye_color))
        print("Month: {0:19} Training: {1}".format(self.Month,self.Training))
        print("-----------------------------")

n = Namebadge()
n.main()