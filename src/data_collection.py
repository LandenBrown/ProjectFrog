import random, time

from frog_species import Frog
from world_biome import Biome
from predator_species import Predator

####Initial Data Creation and Collection Sets

#First names

frog_first_names = ["Foro", "Litho", "Oro", "Morro", "Jerro", "Kiro", "Lero", "Shira", "Geru", "Fortha", "Terelu", "Maxor"]
predator_first_names = ["Veres", "Treves", "Meres", "Heres", "Nores", "Maxes"]

#Middle names
frog_middle_names = ["te", "de", "le", "vur", "lor", "lex", "ret", "vet", "cret", "feg", "van", "vax", "cet", "hat", "setti", "fetti", "cureti"]
predator_middle_names = ["de", "ret", "rat", "raf", "fer", "dur", "lur", "bay", "tray", "tre", "jer"]

#Last names
frog_last_names = ["lithius", "birtius", "crethius", "ferelias", "trallium", "borallian", "sillian", "terillian", "victus", "victillian", "fortillia", "shillia", "camillia"]
predator_last_names = ["relious", "celius", "tricillian", "gorian", "filthian", "vestian", "snichian"]

def create_a_frog_name(fnames, mnames, lnames):
    #getting length of arrays minus 1
    fnamelength = (len(fnames)-1)
    mnamelength = (len(mnames)-1)
    lnamelength = (len(lnames)-1)
    #Generating random number between 1 and length of array
    fnamerandom = random.randint(1, fnamelength)
    mnamerandom = random.randint(1, mnamelength)
    lnamerandom = random.randint(1, lnamelength)
    #Building the random name with random selection in each array
    randomName = fnames[fnamerandom]+mnames[mnamerandom]+lnames[lnamerandom]
    return randomName
def create_a_predator_name(fnames, mnames, lnames):
    #getting length of arrays minus 1
    fnamelength = (len(fnames)-1)
    mnamelength = (len(mnames)-1)
    lnamelength = (len(lnames)-1)
    #Generating random number between 1 and length of array
    fnamerandom = random.randint(1, fnamelength)
    mnamerandom = random.randint(1, mnamelength)
    lnamerandom = random.randint(1, lnamelength)
    #Building the random name with random selection in each array
    randomName = fnames[fnamerandom]+mnames[mnamerandom]+lnames[lnamerandom]
    return randomName


######## FROG DATA
#Internal Attributes
#List:
frog_int_atts = ["Cold Blooded", "Warm Blooded", "Scared", "Brave"]
#
#
#External Attributes
#List:
frog_ext_atts = ["Strong", "Weak", "Fast", "Slow", "Camoflauge", "Smelly"]
#
#
######## PREDATOR DATA
#Internal Attributes
#List:
predator_int_atts = ["Cold Blooded", "Warm Blooded"]
#
#
#External Attributes
#List:
predator_ext_atts = ["Strong", "Weak", "Fast", "Slow"]
#
#



################################################################################      FROGS
def create_an_initial_frog(int_atts, ext_atts):
    ###Calculate Internal Attribute
    #getting length of arrays minus 1
    int_atts_length = (len(int_atts)-1) 
    #Generating random number between 1 and length of array
    RandomIntAtt_spot = random.randint(0, int_atts_length)
    RandomIntAtt = int_atts[RandomIntAtt_spot]
    
    ###Calculate External Attribute
    #getting length of arrays minus 1
    ext_atts_length = (len(ext_atts)-1)
    #Generating random number between 1 and length of array
    RandomExtAtt_spot = random.randint(0, ext_atts_length)
    RandomExtAtt = ext_atts[RandomExtAtt_spot]

    ###Calculate Name
    randomName = create_a_frog_name(frog_first_names, frog_middle_names, frog_last_names)

    ###Calculate Lifespan
    #Set lifespan constraints
    min_lifespan_days = 20
    max_lifespan_days = 100
    #Generate random lifespan
    randomLifespan = random.randint(min_lifespan_days, max_lifespan_days)

    #Generate time to starve
    min_food_days = 2
    min_food_days = 5
    #Gerenate random starvation period
    randomStarvation = random.randint(min_food_days, max_lifespan_days)


    #Generate mate chance per day
    min_mate_chance = 1
    max_mate_chance = 8
    #Generate random mate chance 
    randomMateChance = random.randint(min_mate_chance, max_mate_chance)

    #Generate infertility
    infertileChance = random.randint(1, 100)
    fertility = True
    if infertileChance >= 50:
        fertility = True
    else:
        fertility = False

    #Creat new frog and return it
    return Frog(randomName, RandomExtAtt, RandomIntAtt, 1, randomLifespan, 0, randomStarvation, False, randomMateChance, fertility)
    

#frog1 = create_an_initial_frog(frog_int_atts, frog_ext_atts)
#print(frog1.name,frog1.internal_attributes,frog1.external_attributes,str(frog1.lifespan_days))




    


################################################################################      PREDATORS
def create_an_initial_predator(int_atts, ext_atts):
    ###Calculate Internal Attribute
    #getting length of arrays minus 1
    int_atts_length = (len(int_atts)-1) 
    #Generating random number between 1 and length of array
    RandomIntAtt_spot = random.randint(0, int_atts_length)
    RandomIntAtt = int_atts[RandomIntAtt_spot]
    
    ###Calculate External Attribute
    #getting length of arrays minus 1
    ext_atts_length = (len(ext_atts)-1)
    #Generating random number between 1 and length of array
    RandomExtAtt_spot = random.randint(0, ext_atts_length)
    RandomExtAtt = ext_atts[RandomExtAtt_spot]

    ###Calculate Name
    randomName = create_a_predator_name(predator_first_names, predator_middle_names, predator_last_names)

    ###Calculate Lifespan
    #Set lifespan constraints
    min_lifespan_days = 20
    max_lifespan_days = 200
    #Generate random lifespan
    randomLifespan = random.randint(min_lifespan_days, max_lifespan_days)

    #Creat new frog and return it
    newPredator = Predator(randomName, "Walk", RandomExtAtt, RandomIntAtt, "Bite", randomLifespan, 0, False)
    return newPredator
    
#predator1 = create_an_initial_predator(predator_int_atts, predator_ext_atts)
#print(predator1.name,predator1.internal_attributes,predator1.external_attributes,str(predator1.lifespan_days))




#Here we must figure out how we are going to handle the giant list of frogs that is going to spawn
#For now we will store them in a list and track the name of the frog based on the below logic
##################   NEED TO READ ON DICTIONARIES AS I KNOW ITS GONNA BE THE BEST WAY FORWARD BUT I DONT WANT TO DO IT.
lastFrogNumber = 0
newFrogName = "frog"

#production frog creation... 
#update the lastFrogNumber for tracking
def update_lastFrogNumber():
    global lastFrogNumber
    lastFrogNumber += 1
    completeFrogName = newFrogName+str(lastFrogNumber)
    return completeFrogName

####Testing object creation


# class FrogList:
#     def __init__(self, title, frogs):
#         self.title = title
#         self.data = data
#     def list_frogs(self):
#         print("\n"+self.title)
#         for k in self.data.keys():
#             print("-"*self.data[k]+" "+k)

# data = {"a":4, "b":7, "c":8}
# initial_list = FrogList("Simple Frog List", data)




###Dynamic frog creation steps

#create a dictionary to store frogs in
#Create a name for the key to reference each frog (update last frog number)
#gather what the object attributes are going to be
#Create the actual object
#append it in the dictionary


####Simple game testing

#creating static dict for frogs
frog_dict = {update_lastFrogNumber():create_an_initial_frog(frog_int_atts, frog_ext_atts)}
frog_dict[update_lastFrogNumber()] = create_an_initial_frog(frog_int_atts, frog_ext_atts)
#print(frog_dict["frog1"].name)

#Biomes

standardJungle = Biome("Standard", "Tropical", "Rainforest", "Normal", "Picked", "Consistent", "Standard")

WorldAgeInDays = 0
#Test list iteration as well as find food chance + death
# all(x.is_dead!=True for x in frog_dict.values())
x = 2
while x != 1:
    if x == 3:
        print("No simulation.")
        break
    WorldAgeInDays+=1
    print("It is now day ", str(WorldAgeInDays))
    for frog in frog_dict.values():
        #Let the frog look for food.
        if frog.is_dead == False:
            #Instead of find food, each frog needs to have a RunDailySimulation function that incorporates everything 
            frog.findFood(standardJungle)
            if frog.checkMating():
                #Get list of frogs that are currently alive
                frogsCurrentlyAlive = [v for k,v in frog_dict.items() if v.is_dead == False] 
                #get length of that list minus 1 for list calculation   
                numberOfFrogsCurrentlyAlive = (len(frogsCurrentlyAlive) - 1)
                #pick a random frog in that list
                randomAliveFrog = random.randint(0, numberOfFrogsCurrentlyAlive)
                #Mate with this frog and add to dictionary
                frog.Mate(frogsCurrentlyAlive[randomAliveFrog], create_an_initial_frog)
                #how the fuck do i add this frog to the dictionary
                frog_dict[update_lastFrogNumber()] = frog.Mate(frogsCurrentlyAlive[randomAliveFrog], create_an_initial_frog)
                print("############################### A NEW FROG HAS BEEN BORN")
                #time.sleep(2)
                print(len(frog_dict))
                #time.sleep(2)
                break
                


    if WorldAgeInDays > 5000:
        print("World age is 5000, ending.")
        break
    if all(x.is_dead==True for x in frog_dict.values()):
        print ("the final frog has died.")
        break
    #if all(x.is_dead==True for x in frog_dict.values()):
        #print("THE LAST FROG JUST DIED. EXITING")
        #break

print("All frogs died on day", str(WorldAgeInDays))
print("A total of " + str(len(frog_dict)) + " frogs lived on your planet")
for frog in frog_dict.values():
    print(frog.name)


#Testing grabbing the frogs that are currently alive
#myList = [v.name for k,v in frog_dict.items() if v.is_dead == False]       
#print (myList) 
#works 


    