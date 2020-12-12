import random


class Frog:
    def __init__(self, name, external_attributes, internal_attributes, days_alive, lifespan_days, days_without_food, starvation_days, is_dead):
        self.name = name
        self.external_attributes = external_attributes
        self.internal_attributes = internal_attributes
        self.days_alive = days_alive
        self.lifespan_days = lifespan_days
        self.days_without_food = days_without_food
        self.starvation_days = starvation_days
        self.is_dead = is_dead


    def checkLifespan(self):
        #Check to see if the frog has died of old age yet. 
        if self.days_alive >= self.lifespan_days:
            print("This frog is now dead.")
            #####Kill frog
        else:
            print("This frog is still alive.")


    def checkStarvation(self):
        #check to see if the frog has died of starvation.
        if self.days_without_food >= self.starvation_days:
            print("This frog is now dead.")
            ######Kill frog
        else:
            print("This frog has not starved yet.")


    def findFood(self, biome):
        #Make sure you're alive and not dead of old age.
        self.checkLifespan()
        #Generate a random number 
        foodRandom = random.randint(1, 100)
        #Is the biome food density low
        if biome.food_density == "Low":
            #25% chance of finding food that day
            if foodRandom >= 75: 
                print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()
        #Is the biome food density standard
        if biome.food_density == "Standard":
            #50% chance of finding food that day
            if foodRandom >= 50: 
                print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()
        #Is the biome food density high
        if biome.food_density == "High":
            #50% chance of finding food that day
            if foodRandom >= 75: 
                print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()






    