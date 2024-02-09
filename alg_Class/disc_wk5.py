#Create a Python program that uses a while loop and prompts
#the user for a series of inputs. You should use a sentinel
#value to signal when the loop should terminate. Calculate
#and display the sum of the user inputs.
#Some examples that you might use are the following:

#Total number of miles traveled on a road trip.
#Total cost of groceries in a month.
#Total number of accidents in a year.
#You must choose something different from any of the above, however.

#Include comments in your code program that describe what the program does.
#Submit your code as an attachment (.py file) and post a screenshot of
#executing your program on at least one test case.

#Michael Hall discussion wk5 - 2/6/24

#CONSTANTS----------------------------

#list of reccomended subjects the java developer should know for employment



#list of each divided group of subsections to learn
fundamentals = ["basic syntax","data types","conditionals","loops","exception handling","functions", "data structures","OOP/inheritances/classes","packages","working with files and APIs"]
postFundamentals = ["memory management, collection framework","seralization","networking and sockets","generics","streams","the JVM","garbage collection","thread basics"]
buildTools = ["Gradle","Maven","Ant"]
webFrameworks = ["Spring","Spring boot","play framework","Spark"]
objectRelationalMapping = ["JPA","Spring data JPA","Hibernate","EBean"]
loggingFrameworks = ["SLF4j","TinyLog"]
dataBasePersistence = ["JDBC","JDBI3","JDBC template"]
appTesting = ["unit testing(JUnit/TestNG)","integration testing(REST assured/JMeter","behavior testing(Cucumber-JVM/Cukes/JBehave)"]

#lists for manipulating the above lists in specific form - either as a verbal representation(String usage) or a list that houses each sublist
subjectListName = ["fundamentals", "beyond fundamentals", "build tools","web frameworks","object relational mapping","logging frameworks","data base persistence","app testing"]
subjectListIndex = [fundamentals, postFundamentals, buildTools, webFrameworks, objectRelationalMapping, loggingFrameworks, dataBasePersistence, appTesting]

    #sentVal (numberOfTotalTopics)
totalSubjects = len(subjectListIndex)


#FUNCTIONS----------------------------

#greeting/intro
def greet():
    print("""So you want to learn Java! Wonderful. As a programmer,
you will learn to 'divide and conquer,' so let's start now with our study
plan. There are certain topics you need to cover and come to understand.
Once this is done, you can call yourself a novice and potentially be job ready.\n""")

#brief explanation to user of their progress
#uses a value of completed in comparison with a value of the total to complete, returning a status and comment to user
def statusWithComment(val, allVals):
    if (val == allVals):
        print("You've covered all the topics! Time to focus on Java back end!")
    elif (val > allVals * .9):
        print("\nYour'e over 90% done, the finish line approaches!")
    elif (val > allVals * .8):
        print("\nYour'e over 80% done, keep it up!")
    elif (val > allVals * .7):
        print("\nYour'e over 70% done, you'll be there soon!")
    elif (val > allVals * .6):
        print("\nYou've completed over 60% of the material, keep at it.")
    elif (val > allVals * .5):
        print("\nOver half way done, maintain that momentum!")

    print("(You have completed %d of %d)\n" % (val, allVals))

#add
#def add(val): #<--passes total as value to increment
 #   toAdd = input("\nOf the above-mentioned sub topics, how many do you know?\n")
  #  if (toAdd.is)
    
#goodBye
def goodBye():
    print("""Please review the above mentioned topics that must be learned,
write out your study plan and have at it! You got this.""")


#Main---------------------------------
def main():
    #CONSTANTS------------------------

   #total number of topics to learn
    allSubjects = len(fundamentals)+len(postFundamentals)+len(buildTools)+len(webFrameworks)+len(objectRelationalMapping)+len(loggingFrameworks)+len(dataBasePersistence)+len(appTesting)
    #tracking how many total subjects the user says they understand
    total = 0
    #tracking material known by user 
    known = 0


    while (known < len(subjectListIndex)): #beginning sentVal compared with total number of tipics to be known
        # known will iterate up with each question about one of the topics with the topics list (using string name list)
        for topic in subjectListName:
            response = input("\nHave you learned %s? [y / n]" % (topic))
            if (response == 'y'.lower() or response == 'yes'.lower()):
                print("\nSo you have learned the following?\n")
                #will iterate through each topic within the subjectListIndex list, accessing a list that references the other lists
                for subTopic in subjectListIndex[known]:
                    #the above mentioned 'other lists,' referenced within the subjectListIndex, will now be iterated through themselves
                        print(subTopic)
                add = input("\nOf the above-mentioned sub topics, how many do you know?\n") #increases total (measuring subtopics learned), told to user at the end
                #behaves based on receiving a number or 'number' while preventing error caused by user inputing a non-String number
                if (add.isdigit() and int(add) > 0 and int(add) <= len(subTopic)): 
                    total = total + int(add)
                #this elif protects against user entering a number too high; when this happens the total is added, the user is informed, and the iteration continues
                elif(add.isdigit() and int(add) >= len(subjectListIndex[known])):
                    (print("You entered a value over the total number of subjects, the total number of subjects (%d) for %s will be added)" % (len(subjectListIndex[known]), subjectListName[known])))
                    total = total + len(subjectListIndex[known])
                else:
                    print("There was an invalid entry, all the subtopics from %s will be added to your to-learn list" % (subjectListName[known]))
                known = known + 1 #increments sentVal as each topic to be known is addressed in the loop                 
            else: 
                  print("This will involve learning: \n")
                  for subTopic in subjectListIndex[known]:
                      print(subTopic)
                  total = total #in the case that no subtopics are known, all subtopics are addded to total needed to learn via list's legth value
                  known = known + 1

        statusWithComment(total, allSubjects)


#Run code----------------------------

#CONSTANTS
   #total number of topics to learn
allSubjects = len(fundamentals)+len(postFundamentals)+len(buildTools)+len(webFrameworks)+len(objectRelationalMapping)+len(loggingFrameworks)+len(dataBasePersistence)+len(appTesting)
    #tracking how many total subjects the user says they understand
total = 0
    #tracking material known by user 
known = 0    
greet()
    
main()

goodBye()