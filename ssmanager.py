def studentAverageScore(students):#students is now a list of tuples that contains name and score
    if len(students) == 0:
        return 0
    
    totalscore = 0#define a var to begin the loop
    for student in students:
        totalscore += int(student[1]) 
    return totalscore / len(students)    
    
def getHighestScoreStudent(students):
    if len(students) == 0:
        return None #or 0 but here we have to return an object not a int
    
    highestScoreStudent = students[0]
    for student in students:
        if int(student[1]) > int(highestScoreStudent[1]):
            highestScoreStudent = student
    return highestScoreStudent

def getAllWithScoreBelow(stduents, belowNb):
    belowNbStudents = []
    for student in students:
        if int(student[1]) < belowNb:
            belowNbStudents.append(student)
    return belowNbStudents
def Sum_Scores_Recursive(scores):
    if len(scores)== 0: #or if scores=[] or if not scores:
        return 0 #0 implies that there is no score (base case)
    else:
        return scores[0] + Sum_Scores_Recursive(scores[1:]) #recursive case
################ main program ##########

numberInput = int(input("how many student did you want to add? "))#ask the user about number of students
students = []
for i in range (numberInput):
    nameinput = input("enter student name:")
    scoreinput = input("enter student score:")
    students.append(tuple([nameinput, scoreinput]))#here i append a tuple that contains name and score on each index

print("All students and scores:")
for student in students:
    print(student[0], "-" ,student[1])

print("Average score:",studentAverageScore(students))
highestScoreStudent = getHighestScoreStudent(students)
print("Top student:", highestScoreStudent[0], "(", highestScoreStudent[1] ,")")

failedStudents = getAllWithScoreBelow(students, 55)
for student in failedStudents:
    print("Failed student:", student[0])

score = [int(student[1]) for student in students] #now the editor should fill the score list

SumOfScores = Sum_Scores_Recursive(score) #here i call the fuction
print("sum of the scores using recursion is :" , SumOfScores)#finally i print the sum