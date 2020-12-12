import random


class Frog:
    def __init__(self, name, external_attributes, internal_attributes, days_alive, lifespan_days, days_without_food, starvation_days, is_dead, mate_chance, infertile):
        self.name = name
        self.external_attributes = external_attributes
        self.internal_attributes = internal_attributes
        self.days_alive = days_alive
        self.lifespan_days = lifespan_days
        self.days_without_food = days_without_food
        self.starvation_days = starvation_days
        self.is_dead = is_dead
        self.mate_chance = mate_chance
        self.infertile = infertile


    def checkLifespan(self):
        #Check to see if the frog has died of old age yet. 
        self.days_alive+=1
        if self.days_alive >= self.lifespan_days:
            print("###################################   A FROG HAS DIED OF OLD AGE")
            self.is_dead = True
            #####Kill frog
    


    def checkStarvation(self):
        #check to see if the frog has died of starvation.
        if self.days_without_food >= self.starvation_days:
            print("###################################   A FROG HAS DIED OF STARVATION")
            ######Kill frog
            self.is_dead = True

    def checkMating(self):
        #Check to see if the frog is fertile or not
        if self.infertile == True:
            #print("This frog is infertile")
            pass
        else:
            #generate random number between 1-100 for mate chance potential comparison
            mateComparison = random.randint(1,100)
            if self.mate_chance >= mateComparison:
                #print("######################### A NEW FROG CAN MATE")
                return True
            else:
                return False
    
    def Mate(self, x, initializeFrog):
        #Grab an internal and external attribute from the other frog
        new_int_att = x.internal_attributes[0]
        new_ext_att = x.external_attributes[0]
        #Grab an internal and external attribute from myself 
        self_int_att = self.internal_attributes[0]
        self_ext_att = self.external_attributes[0]

        #Combine the lists into an interal_atts list and an eternal_atts list
        internal_atts = []
        internal_atts.append(new_int_att)
        internal_atts.append(self_int_att)
        external_atts = []
        external_atts.append(new_ext_att)
        external_atts.append(self_ext_att)

        return initializeFrog(internal_atts, external_atts)



        


    


    def findFood(self, biome):
        #Make sure you're alive and not dead of old age.
        self.checkLifespan()
        #Generate a random number 
        foodRandom = random.randint(1, 100)
        #Is the biome food density low
        if biome.food_density == "Low":
            #5% chance of finding food that day
            if foodRandom >= 95: 
                #print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                #print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()
        #Is the biome food density standard
        if biome.food_density == "Standard":
            #10% chance of finding food that day
            if foodRandom >= 90: 
                #print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                #print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()
        #Is the biome food density high
        if biome.food_density == "High":
            #15% chance of finding food that day
            if foodRandom >= 85: 
                #print("We have found food.")
                #Set days without food to 0
                self.days_without_food = 0
            else: 
                #print("We have not found food today.")
                #Set days without food to + 1
                self.days_without_food += 1
                #check starvation status
                self.checkStarvation()






    