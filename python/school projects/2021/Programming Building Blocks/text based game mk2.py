
#%%
class Game:

    def main(self):
        print()
        print("Welcome to the ELEMENTAL DUNGEON!  This is a text adaptation of another videogame I am developing.")
        print("You start in the first room of the dungeon, the Trial of fire!  I hope you enjoy!")
        print("there are four endings in this demo, see if you can find them all!")
        print()
        print()
        tof = self.Trial_Of_Fire()
        tof.start()
        
    def game_over(self,room):
        print()
        print("----GAME OVER----")
        print(f"You died to {room}")
        print("--Press 1 to restart--")
        if input() == 1:
            self.main()

    class Player:

        def __init__(self):
            self.player_description = "It is you."
            self.inventory = ['bucket of water','codex','bread','firewood']
            self.equipment_list = ['leather armor','steel sword']
            self.equipment = {"Armor": "Leather Armor","Weapon": "Steel Sword"}
            self.tags = []
            self.room = 1
            self.mood_change = 0

        def use_item(self):
            print("What item would you like to use?  ")
            use = input("Item: ")
            if use in self.inventory:
                print(f"You use {use}")
                print()
                self.item_actions(self.room,use)
                return
            else:
                print(f"You don't have {use} in your inventory.")
                return

        def use_equipment(self):
            print("What piece of equipment would you like to use?  ")
            use = input("Item: ")
            use = use.lower()
            if use in self.equipment_list:
                print(f"You use {use}")
                print()
                self.item_actions(self.room,use)
                return
            else:
                print(f"You don't have {use} in your inventory.")
                return   

        def display_inventory(self):
            print()
            print("Inventrory:")
            for item in self.inventory:
                print(f"{item}")
            return

        def display_equipment(self):
            print()
            print("Equipment:")
            for item in self.equipment:
                print(f"{item}: {self.equipment.get(item)}")
            return

        def item_actions(self,room,use):
            if use == 'bread':
                print()
                print("You are not hungry right now.")
            if use == 'firewood':
                if room == 1:
                    self.mood_change += .5
                    print()
                    print('---firewood removed---')
                    print("You pull the firewood from your bag, tossing it into the flames. It is quickly consumed.")
                    print("Nigma's voice seems supprised, as they speak.")
                    print("THANK YOU FOR YOUR OFFERING MORTAL.  IT IS CERTAINLY APPRECIATED. It IS NOT OFTEN I AM GIVEN AN OFFERING.")
                    self.inventory.remove('firewood')
                    return                   
            if use == 'codex':
                if room == 1:
                    print("how would you like to use the codex?")
                    print("1. Read information on Nigma.")
                    print("2. Throw the codex in the flames.")
                    choice = int(input("Selection:  "))
                    if choice == 1:
                        print()
                        print("The codex describes Nigma as a kind spirit, though their nature makes them a danger to be around.")
                        print("They accept offerings of flammable material, but really enjoy a good conversaion.")
                        return
                    if choice == 2:
                        print()
                        print("You toss the codex into the flames.  It does not burn, though Nigma reaches down to pick it up. They then speak.")
                        print("'THIS IS A PRECIOUS ARTIFACT, ARE YOU SURE YOU WISH TO GIVE IT AS AN OFFERING?")
                        confirmaion = str(input("Are you sure? (y/n) "))
                        confirmaion = confirmaion.lower()
                        if confirmaion == 'y':
                            print()
                            print('---codex removed---')
                            print("VERY WELL MORTAL. I AM IMPRESSED, NOT MANY WOULD BE WILLING TO DISCARD SUCH A VALUABLE ITEM")
                            self.inventory.remove('codex')
                            self.mood_change += .5
                            return
                        else:
                            print("Nigma reaches down, placing the codex back at your feet.")
                            print("I AM DISAPPOINTED YOU WERE NOT WILLING TO PART WITH IT, BUT I UNDERSTAND WHY YOU WISH TO KEEP IT.")
                            print("they seem frustrated.")
                            self.mood_change -= .5
            if use == 'bucket of water':
                if room == 1:
                    print("How would you like to use the bucket?")
                    print("1: Pour water on yourself.")
                    print("2: toss water at Nigma")
                    selection = int(input("choice:"))
                    if selection == 1:
                        print()
                        self.inventory.remove("bucket of water")
                        self.inventory.append("empty bucket")
                        self.tags.append('wet')
                        print("--- item removed: Bucket of Water ---")
                        print("--- item added: Empty Bucket ---")
                        print("--- you gained chariteristic: Wet ---")
                        print("You pour the water over yourself, soaking your armor and body in cool water.")
                        return
                    if selection == 2:
                        print()
                        print("With all your might, you fling the water at Nigma.  It evaporates before it can make contact")
                        print("'WHAT EXACTLY WERE YOU TRYING TO DO THERE?' Nigma's voice boomes out, the flames flareing.")
                        self.inventory.remove("bucket of water")
                        self.inventory.append("empty bucket")
                        self.mood_change -= 1
                        print("--- item removed: Bucket of Water ---")
                        print("--- item added: Empty Bucket ---")
                        return                     
            if use == 'steel sword':
                print("that wont be much use here")
                return           
            if use == 'leather armor':
                print("that wont be much use here")
                return
            
            return

    class Trial_Of_Fire:

        def __init__(self):
            self.p = Game.Player()
            self.room_description_start = "This simple circular room is composed completely out of chared stone, polished to an obsidian shine.\nIn its center sits a stone pillar, about waist high, with a glowing red gemstone sitting atop it."
            self.room_description = "This simple circular room is composed completely out of chared stone, polished to an obsidian shine.\nIn its center sits a stone pillar, about waist high, with a glowing red gemstone sitting atop it.\nFlames surround this pillar, making it difficult to see the gemstone."
            self.elemental_description = "Nigma, the guardian of the flame.  Composed of multicolord flames that reach up to the ceiling, this \nbeeing of fire radiates a powerfull heat.  They are a powerfull spirit."
            self.room_actions = {
                "grab gemstone": self.grab_gemstone,
                "take gemstone": self.grab_gemstone,
                "use item": self.p.use_item,
                "use equipment": self.p.use_equipment,
                "equipment": self.p.display_equipment,
                "inventory": self.p.display_inventory,
                "talk": self.talk,
                "help": self.help,
                }
            self.Nigma_mood = 3

        def start(self):
            print(self.room_description_start)
            print("As you enter the room, a massive being composed of flames erupts from the gemstone, filling most of the room.  Supprised,\nyou try to back out of the room, but the door seems to have closed behind you.")
            print()
            print("A booming voice emanates from the being of fire:\n'WELCOME TO THE TRIAL OF FLAME!'\nit pauses for a moment.\n'OR FIRE, OR WHATEVER WE ARE CALLING IT THESE DAYS.")
            print("'I AM NIGMA, GUARDIAN OF THE FLAME!  BY ENTERING THIS DUNGEON YOU HAVE ALREADY PROVEN YOU HAVE A STRONG DESIRE,\nBUT YOU MUST NOW PROVE TO ME THAT YOU DESERVE TO HAVE THAT WISH FULFILLED!'")
            print("The flaming figure rases its arms to the sides, as if in challenge.")
            self.main()

        def main(self):
            self.Nigma_mood += self.p.mood_change
            self.p.mood_change = 0
            print()
            print()
            print("What would you like to do?")
            choice = input("Action: ")
            choice = choice.lower()
            self.switch(choice)
            self.main()

        def grab_gemstone(self):
            print()
            if "wet" in self.p.tags: 
                print("Steam boils off you as you approach, and while its far from comfortable, you are unharmed as you reach the pillar.")
                print("With a swift motion, you plunge your hands into the fire, grabbing the gemstone in your fist.  Its warm to the touch.")
                self.end(1)
                return
            if "metal armor" in self.p.equipment: 
                print("You move twards the pilar carefully.  Between the cloth padding and metal outside of the armor, you are able to reach the pillar unharmed.")
                print("With a swift motion, you plunge your hands into the fire, grabbing the gemstone in your fist.  Its warm to the touch.")
                self.end(2)
            else:
                print("You approach the pillar, arms rased against the heat.  You can feel your body begining to burn as you reach the pillar.")
                if self.Nigma_mood == 3:
                    self.p.tags.append("burned")
                    print("You plunge your hand into the flame, swiping the gemstone off its pillar.  while the stone is warm, its cool in comparison\nto the burns you now have accross your body.")
                    self.end(3)
                if self.Nigma_mood > 3:
                    self.p.tags.append("Flame-blessed")
                    print("You plunge your hand into the flame, swiping the gemstone off tts pillar.  The moment your fingers make contact with the gem,\na comforting warmth blossoms within you.")
                    self.end(4)
                if self.Nigma_mood < 3:
                    print("As you approach the pillar, a wall of flame erupts before you, forcing you back. Nigma's booming voice echoes around the chamber.")
                    print("'YOU ARE NOT WORTHY OF MY POWER! FOR YOUR PRESUMPTION, YOU WILL BE PUNISHED!'")
                    print("The flames around you begin to burn hotter and hotter, burning away first your sweat, then your hair, then finlay your body.")
                    print("you take your last breath.")
                    Game.game_over(Game,"Trial of Fire")

        def default(self):
            print("Im sorry, but I don't understand that request.")
            print("you can type 'HELP' to get help with actions")
            self.main()

        def switch(self,action):
            print()
            print()
            return self.room_actions.get(action,self.default)()

        def end(self,ending):
            endings = [1,2,3,4]
            if ending == 1:
                #neutural ending using the waterskin
                print()
                print("You quickly jump back from the pillar, but you suddenly realise that the room's heat no longer bothers you.")
                print("Nigma's flames still fill the room, but their intensity seems muted, allowing you to see them for their beauty.")
                print("Nigma's flaming body shrinks your size then, a clear humanoid form that approaches you.  They stop only a few paces from you.")
                print()
                print("'Well done.  You have proven your bravery to me.  You had no way to know if that splash of water would protect you,\nbut you were willing to try anyways. Go forth with my blessing.")
                print()
                print("Nighma seems disappointed, but gestures to the back of the room as ash and char broke free from the stonework, revealing a stone doorway.")
                print("'Go now, and complete your quest' Nigma says, fading to smoke and leaving you alone.")           
            if ending == 2:
                #neutural ending useing the fullplate
                print()
                print("You quickly jump back from the pillar, but you suddenly realise that the room's heat no longer bothers you.")
                print("Nigma's flames still fill the room, but their intensity seems muted, allowing you to see them for their beauty.")
                print("Nigma's flaming body shrinks your size then, a clear humanoid form that approaches you.  They stop only a few paces from you.")
                print()
                print("'Well done.  You have proven your bravery to me.  You had no way to know if that armor would protect you,\nbut you were willing to try anyways. Go forth with my blessing.")
                print()
                print("Nighma seems disappointed, but gestures to the back of the room as ash and char broke free from the stonework, revealing a stone doorway.")  
                print("'Go now, and complete your quest' Nigma says, fading to smoke and leaving you alone.")      
            if ending == 3:
                #neutural ending with neutural mood
                print()
                print("You quickly jump back from the pillar, collapsing onto the floor.  The room's heat no longer bothers you, though your burns")
                print("still sting.  Nigma's flames fade to nothing and the room begins to cool down. Their body shrinks to one only a head or two taller")
                print("than yourself.  You are supprised to see the detail in their body as they approach you, concern on their face. They kneel before you.")
                print()
                print("'You have proven your bravery, but it has cost you dearly.  I am sorry I could not temper the flame for you my\nchild, but you have my blessing. Go forth, but remember to take caution. I am more gentle then most.'")
                print()
                print("Nigma seems sad as they gesture to the back of the room. Ash and char break free from the stonework, revealing a stone doorway.")
                print("'Go now, and complete your quest' Nigma says, fading to smoke and leaving you alone.")
            if ending == 4:
                #good ending
                print()
                print("You step back from the pillar slowly, stunned as the warmth spreads thruought your body. You watch in shock as")
                print("your burns begin to fade, a golden flame spreading accross them.  It is soothing, and soon you feel yourself stronger then before.")
                print("Nigma's form shrinks to your height, and approaches arms open.  A wide smile covers their face, and their voice is full of excitement.")
                print()
                print("'Excellently done my child! You not only proved your bravery by reaching into those flames, but you proven to me that you are worthy.\nYou are worthy of not just my blessing, but a portion of my power as well.'")
                print()
                print("Nigma gestures to the back of the room. Ash and char broke free from the stonework, revealing a stone doorway.")
                print("'Go now, and complete your quest.  I will be with you!' Nigma says.  They shrink to the size of a match flame before\nphasing into the gemstone, causing it to glow with red light.")
            if ending in endings:
                print()
                print('--- TRIAL OF FIRE CLEARED! GEMSTONE OBTAINED! ----')
                print()
                print("Thank you for playing!  As was mentioned, this is part one of a video game I have been developing, converted into a text based game.")
                print("I hope you enjoyed!")

        def help(self):
            print()
            print("to make a selection, type in the action you would like to do, such as 'use -item-' or 'inspect -detail-")
            print("would you like me to display an exact list of actions? (y/n)")
            choice = input("Display possible actions:  ")
            choice = choice.lower()
            if choice == 'y':
                for item in self.room_actions:
                    print(item)
            self.main()

        def talk(self):
            print()
            print("Nigma is supprised that you wish to talk.  Not many offer to just talk with them.")
            print("They suppress their flames, leaving the room confortably warm, though the pillar is still engulfed in flame.")
            print()
            print("WHAT IS IT THAT YOU WOULD LIKE TO DISCUSS?")
            print("1. Discuss the world")
            print("2. Insult them")
            discussion_choice = int(input("Choice:  "))
            if discussion_choice == 1:
                print()
                print("You spend hours talking with Nigma, discussing the world and all the many intersting things in it.")
                print("After spending some time in conversaion, Nigma ends the discussion.")
                print("THANK YOU FOR GIVING ME THE OPPORTUNITY TO LEARN MORE OF YOUR WORLD.  IT IS NOT OFTEN I GET TO SEE IT.")
                self.Nigma_mood += 1
                return
            if discussion_choice == 2:
                print()
                print("You arent quite sure what insults would work on an elemental such as Nigma, so you try a few.")
                print("YOU DARE INSULT ME!?!  AFTER I ALLOWED YOU INTO THIS CHAMBER?  THE NERVE!")
                self.Nigma_mood -= 1
                return

g = Game()
g.main()

# %%
