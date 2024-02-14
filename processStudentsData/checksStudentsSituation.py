from math import ceil

STUDENTS_ABSCENCES_COLUMN: int = 2
STUDENTS_GRADES_FIRST_COLUMN: int = 3
NUMBER_OF_GRADES: int = 3

#Checks each student to see their situation and updates the values accordingly
def ChecksAprovalSituation(values: list, totalOfClasses: int) -> list:
    gradeForApprovalInFinals: int = 0
    averageGrade: int

    print("Updated students situation:")
    for student in values:
        averageGrade = GetAverageGrade(student)
        gradeForApprovalInFinals = 0
        
        #First checks if the student failed because of abscences
        if(FailedByAbscences(student, totalOfClasses)):
            student.append("Reprovado por Falta")
            student.append(gradeForApprovalInFinals)
        
        #Then checks if the student has a sufficient average to be approved
        elif(averageGrade >= 70):
            student.append("Aprovado")
            student.append(gradeForApprovalInFinals)

        #Checks if the students can attend to the final exam and calculates the grade it needs to be approved
        elif(averageGrade >= 50 and averageGrade < 70):
            gradeForApprovalInFinals = GetGradeForApprovalInFinals(averageGrade)
            student.append("Exame Final")
            student.append(gradeForApprovalInFinals)
            
        #If none of the previous if's was activated, then the student failed because of its grades
        else:
            student.append("Reprovado por Nota")
            student.append(gradeForApprovalInFinals)
        print(student)

    return values


def FailedByAbscences(student, totalOfClasses) -> bool:
    #Minimum frequency: 25% of classes
    studentAbscences: int = student[STUDENTS_ABSCENCES_COLUMN]

    return (float(studentAbscences) > totalOfClasses * 0.25)


def GetAverageGrade(student) -> int:
    averageGrade: float = 0

    for i in range(NUMBER_OF_GRADES):
        averageGrade += int(student[i + STUDENTS_GRADES_FIRST_COLUMN])
    
    averageGrade /= NUMBER_OF_GRADES
    averageGrade = ceil(averageGrade)

    return int(averageGrade)


def GetGradeForApprovalInFinals(averageGrade) -> int:
    #50 <= (averageGrade + finalExamGrade) / 2
    return (50*2) - averageGrade