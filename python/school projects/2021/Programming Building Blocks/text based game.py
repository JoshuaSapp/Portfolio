#%%
from typing import ClassVar

class game:

    def __init__(self):
        self.BAG = ['JOURNAL','POKET WATCH','BREAD','WATER']
        self.EQUIPMENT = ['LEATHER ARMOR',None,'SWORD',None]
        self.ROOM = 0
        self.PLAYER_STATE = None

    def run(self):
        print()
        print("Welcome to the dungon of the elements!  Many have entered but none have returned!")
        print("it is said that in the depths of the dungeon is the power to change the world!")
        print("what is it that you have come here to change? (press enter to continue)")
        input()
        print()
        print()
        print("you came ready to deal with many dangers, but you dont know what it is you will face.")
        print("As you prepare to enter the dungeon, you realise that your pack is only big enough for four items.")
        print("You currently have:")
        print()
        self.list_bag()
        print()
        print(f"You also have equiped:")
        print()
        self.list_equipment()
        print()
        print()
        print('You take a deep breath, then enter the dungeon')
        print()
        print()
        self.ROOM += 1
        self.room_1_entrance()

    def room_1_entrance(self):
        print("The first room has writing over its door that says 'the trial of fire'")
        print("would you like to use an item before entering the room? (Y/N))")
        choice_1 = input("choice:  ")
        choice_1 = choice_1.lower()
        if choice_1 == 'y':
            print("Would you like to use something from your BAG or EQUIPMENT")
            choice_2 = input("choice:  ")
            choice_2 = choice_2.lower()
            if choice_2 == 'bag':
                print("your bag contains:")
                self.list_bag()
                print()
                print("What item would you like to use?")
                choice_3 = input("choice:   ")
                choice_3 = choice_3.lower()
                self.use_item(choice_3)
            if choice_2 == 'equipment':
                print("you have equiped:")
                self.EQUIPMENT()
                print()
                print("What item would you like to use?")        
                choice_3 = input("choice:   ")        
                choice_3 = choice_3.lower()
                self.use_equipment(choice_3)
        print()
        print("you are ready.  You push open the door.")
        self.ROOM += 1
        self.room_1_main()

    def room_1_main(self):
        print()
        print("-----THE TRIAL OF FIRE------")
        print()
        print("You enter the first room.  It is a simple room made of black chared stone, polished to an obsidian shine.")
        print("The room is perfectly circular, centered on a waist high stone pillar. A simple red gemstone sits on the pillar's top.")
        print("As you step into the room, the top of the pillar ignites, a massive human shaped being forming out of flames of all colors.")
        print()
        print("'WELCOME TRAVELER!!  I AM NIGMA, GUARDIAN OF THE FIRE.  PROVE YOURSELF TO ME, AND EARN YOUR BOON!' it boomed, waves of heat")
        print("radeating off of its body.  While the room had been cool when you had first entered, it was now quickly warming up.")
        print("You knew you would need to be quick.")
        print()
        print()
        print("Options:")
        print("1. ")

    def list_bag(self):
        slot = 1
        for item in self.BAG:
            print(f"slot {slot}: {item}")
            slot += 1

    def list_equipment(self):
        print(f"Armor: {self.EQUIPMENT[0]}")
        print(f"Shield: {self.EQUIPMENT[1]}")
        print(f"Melee Weapon: {self.EQUIPMENT[2]}")
        print(f"Ranged Weapon: {self.EQUIPMENT[3]}")

    def use_item(self,item):
        
        if self.ROOM == 0:
            #Possible entrance uses
            switch = {


            }
        if self.ROOM == 1:
            #Possible trial of fire entrance uses
            pass
        if self.ROOM == 2:
            #Possible trial of fire uses
            pass
        if self.ROOM == 3:
            #Possible post trial of fire uses
            pass
        if self.ROOM == 4:
            #Possible entrance uses
            pass

    def use_equipment(self,item):
        pass

g=game()
g.run()

# %%
