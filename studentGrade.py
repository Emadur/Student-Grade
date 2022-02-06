#This program is about calculating student grade based on Marks
#Will print maximum score, minimum score, overall average and Grade of that student

def main(): #Creating main function
    choice = 'y' #Taking default choice is y for atleast 1 student
    file = open("output.txt", "w+") #Opening the file to enter the student details into output file
    #This program will take student name and marks until the choice is given n/N which means No
    while(choice.lower() == 'y'): #While choice is y
        student_name = input("Enter student name: ")
        while (student_name == "" or student_name == " "): #Checking student name is not spaces
            student_name = input("Enter student name: ")
        print("Enter Student Marks (0-100): ")
        maths = int(input("Maths: ")) #Taking input from user for maths subject
        #If it is not valid input, will again ask user to enter the input
        while (maths < 0 or maths > 100):
            print("Enter grades between(0-100)")
            maths = int(input("Maths: "))
        english = int(input("English: ")) #Taking input from user for english subject
        while (english < 0 or english > 100):
            print("Enter grades between(0-100)")
            english = int(input("English: "))
           #Same like maths taking input for physics, history and biology
        physics = int(input("Physics: "))
        while (physics < 0 or physics > 100):
            print("Enter grades between(0-100)")
            physics = int(input("Physics: "))
        history = int(input("History: "))
        while (history < 0 or history > 100):
            print("Enter grades between(0-100)")
            history = int(input("History: "))
        biology = int(input("Biology: "))
        while (biology < 0 or biology > 100):
            print("Enter grades between(0-100)")
            biology = int(input("Biology: "))
        #Calculating minimum value by calling minimum_marks function and passing all the marks as arguments
        minimum = minmum_marks(maths, english, physics, history, biology)
        #Calculating maximum value by calling maximum_marks function and passing all the marks as arguments
        maximum = maximum_marks(maths, english, physics, history, biology)
        #Calculating average of all the marks by calling average_of_marks function
        average = average_of_marks(maths, english, physics, history, biology)
        file.write("Student: "+student_name+"\n") #Writing student name into output file
        file.write("Students minimum mark: "+str(minimum)+"\n") #Writing student marks into output file
        file.write("Students maximum mark: "+str(maximum)+"\n") #Writing maximum marks into output file
        file.write("Student average score: "+str(average)+"\n") #Writing average into output file
        #Below code will write the student grade into output file
        if(average>=90):
            file.write("Student Grade is A \n")
        elif(average>75 and average<90 ):
            file.write("Student Grade is B \n")
        else:
            file.write("Student Grade is C \n")
        file.write("\n")


        choice=input("Do you wish to continue (Y/N)?: ")
    file.close()


def minmum_marks(s1, s2, s3,s4,s5): #Taking 5 subjects as parameters from main function
    minimum = 999 #Taking base value
    for i in s1, s2, s3, s4, s5: #For each subject
        if(i<minimum): #Comparing each subject for minimum value
            minimum = i
    return minimum #Returning minimum value

#This is same as minimum function
def maximum_marks(s1, s2, s3, s4, s5):
    maximum = 0
    for i in s1, s2, s3, s4, s5:
        if (i > maximum):
            maximum = i
    return maximum

def average_of_marks(s1, s2, s3, s4, s5):
    average = (s1+s2+s3+s4+s5)/5 #Calculating average by summing all and dividing by 5
    return average

main() #Calling main function first to execute
