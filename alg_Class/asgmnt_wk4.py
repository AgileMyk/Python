#updated wk3 assignment



#Michael Hall -- 1/2/5 -- Calculate cost for house cleaning IMPROVED
#wk4 changes are noted in comments
#Some of the changes I made involved adjusting the layout order of this program in a way that would seem most sensical to stranger reading my program
#I decided to add commentary and be more robust in the comments I write
#This was motivated less by the programing aspect and more by the comments you left on my grade regarding the first version
#Points were deduced for design only and so I decided to be bring the 'spirit of design' into my coding
#To go immediately to any week 4 changes, you can use the find function and type 'wk 4 change'


def main():
 

#prompt users for values needed to calculate cost
    print("""We have two approaches to cleaning. If you prefer, we can
      do a deep clean; we will require that all members are out of the
      house for an extended period of time (8 hours+) while we devote
      a large amount of effort to deep cleaning the house. This 'bulk'
      purchase will reduce certain costs. The other option, a general
      cleaning, typically lasts for no more than 4 hours, does not require
      anyone to be out of the house, and runs the standard rate.\n\n""")
    

#calculation process based on user decision
    cleanChoice()
    

#functions
def cleanChoice():
    choice = input("Please type 1 for standard cleaning and 2 for deepcleaning (the word or associated number)\n")
    if (choice == "1"):
        roomCount()
    elif (choice == "2"):
        deepCleanCalc()
    else:
        cleanChoice()

        #functions below grouped by the selections in the cleanChoice function, 1 or 2


#regular calculations
#----selection 1 functions---------------------------------------------------------
def roomCount():
    total = 0
    roomTotal = input("How many rooms would you like cleaned?\n")
    if (roomTotal.isdigit()):
        roomTotal = int(roomTotal)
        if roomTotal < 0 or roomTotal > 25:
            print("the room number must be greater than 0 and less than 25")
            roomCount()
        else:
            while int(roomTotal) > 0:
                # current variable created to help properly adjust number of selections made by user in the case of proper and improper input values [wk4 change]
                current = total
                total += roomAsk()
                # introduced this check to prevent user entries being decremented if the user enters an invalid answer that still causes decrement to occur [wk 4 change]
                if (current != total):
                    roomTotal -= 1
            print("\nThe total cost will be", total)
    else:
        print("Please enter a valid numerical value (1-25)")
        roomCount()

#inner function for querying room type
def roomAsk():
    #ask number of times based on room number entered
    #option to enter via verbal input or an associated number input
    #calculates total cost of all rooms
    #constants

    #prices
    ENTRY_WAY_COST = 20
    KITCHEN_COST = 25
    LIVING_ROOM_COST = 30
    DINING_ROOM_COST = 30
    FULL_BATH_COST = 25
    HALF_BATH_COST = 15
    GARAGE_COST = 35
    STUDY_COST = 20
    SUN_ROOM_COST = 25
    HALLWAY_COST = 10
    STEPS_COST = 10
    
    total = 0
    room = input("""Please enter the room type to be cleaned:
    entry way (1), kitchen (2), living room(3),
    dining room(4), full bath(5), half bath(6),
    garage(7), study(8), sun room(9), hallway(10), steps(11)
    """)

    
    #calculates new total, adding the value of each user choice to
    #(beginning list of constant price values in program)
    #the amount of the variable total's current value, updating total each time
    if (room == "entry way".lower()):
        total += ENTRY_WAY_COST
        print(room.lower() + ":", ENTRY_WAY_COST)
    elif (room == "1"):
        total += ENTRY_WAY_COST
        print("entry way:", ENTRY_WAY_COST)
        #KITCHEN
    elif (room == "kitchen".lower()):
        total += KITCHEN_COST
        print(room.lower() + ":", KITCHEN_COST)
    elif (room == "2"):
        total += KITCHEN_COST
        print("kitchen:", KITCHEN_COST)
        #LIVING ROOM
    elif (room == "living room".lower()):
        total += LIVING_ROOM_COST
        print(room.lower() + ":", LIVING_ROOM_COST)
    elif (room == "3"):
        total += LIVING_ROOM_COST
        print("living room:", LIVING_ROOM_COST)
        #DINING ROOM
    elif (room == "dining room".lower()):
        total += DINING_ROOM_COST
        print(room.lower() + ":", DINING_ROOM_COST)
    elif (room == "4"):
        total += DINING_ROOM_COST
        print("dining room:", DINING_ROOM_COST)
        #FULL BATH
    elif (room == "full bath".lower()):
        total += FULL_BATH_COST
        print(room.lower() + ":", FULL_BATH_COST)
    elif (room == "5"):
        total += FULL_BATH_COST
        print("full bath:", FULL_BATH_COST)
        #HALF BATH
    elif (room == "half bath".lower()):
        total += HALF_BATH_COST
        print(room.lower() + ":", HALF_BATH_COST)
    elif (room == "6"):
        total += HALF_BATH_COST
        print("half bath:", HALF_BATH_COST)
        #GARAGE
    elif (room == "garage".lower()):
        total += GARAGE_COST
        print(room.lower() + ":", GARAGE_COST)
    elif (room == "7"):
        total += GARAGE_COST
        print("garage:", GARAGE_COST)
        #STUDY
    elif (room == "study".lower()):
        total += STUDY_COST
        print(room.lower() + ":", STUDY_COST)
    elif (room == "8"):
        total += STUDY_COST
        print("study:", STUDY_COST)
        #SUN ROOM
    elif (room == "sun room".lower()):
        total += SUN_ROOM_COST
        print(room.lower() + ":", SUN_ROOM_COST)
    elif (room == "9"):
        total += SUN_ROOM_COST
        print("run room:", SUN_ROOM_COST)
        #HALLWAY
    elif (room == "hallway".lower()):
        total += HALLWAY_COST
        print(room.lower() + ":", HALLWAY_COST)
    elif (room == "10"):
        total += HALLWAY_COST
        print("hallway:", HALLWAY_COST)
        #STEPS
    elif (room == "steps".lower()):
        total += STEPS_COST
        print(room.lower() + ":", STEPS_COST)
    elif (room == "11"):
        total += STEPS_COST
        print("steps:", STEPS_COST)
        #
    else:
        print("""Please choose a valid room type or enter the associated number:
                entry way: 1,
                kitchen: 2,
                living room: 3,
                dining room: 4,
                full bath: 5,
                half bath: 6,
                garage: 7,
                study: 8,
                sun room: 9,
                hallway: 10,
                steps: 11
              """)

    return total
    
    



#deep-clean calculations
#----selection 2 functions---------------------------------------------------------
def deepCleanCalc():
    LOW = 1500
    MED = 2500
    sqFt = eval(input("""Deep clean pricing is based on square footage and is not impacted
by room type. What is the square footage of the house?\n"""))
    #calc cost and account for minimum pay
    #added a range to test for appropriate print to user to help user understand program [wk 4 change]
    #added '<= 0' condition to protect against that invalid entry potential [wk 4 change]
    if sqFt <= 0:
        print("Please enter a valid positive square footage value\n")
        deepCleanCalc()
    elif sqFt < (LOW * .6):
        print("Our minimum charge to clean is 200")
    elif sqFt < LOW and sqFt * .15 <= 200:
        print("The total cost will be $200")
    elif sqFt < LOW and sqFt * .15 > 200:
        print("The total cost will be $%2d" % (sqFt * .15))
    elif sqFt < MED:
        print("The total cost will be $%2d" % (sqFt * .35))
    else:
        print("The total cost will be $%2d" % (sqFt * .55))
    

#run program main------------------------------------------------------------------
main()