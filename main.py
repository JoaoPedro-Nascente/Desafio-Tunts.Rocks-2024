from sheetsManagment.connection import Stablishes_connection
from sheetsManagment.manageSheets import ReadStudentsData
from sheetsManagment.manageSheets import UpdateStudentsData
from sheetsManagment.manageSheets import GetTotalNumberOfClasses
from processStudentsData.checksStudentsSituation import ChecksAprovalSituation

def main():
    spreadSheetService: any
    studentsData: list
    updatedStudentsData: list
    totalOfClasses: int

    spreadSheetService = Stablishes_connection()

    studentsData = ReadStudentsData(spreadSheetService)
    totalOfClasses = GetTotalNumberOfClasses(spreadSheetService)

    updatedStudentsData = ChecksAprovalSituation(studentsData, totalOfClasses)

    UpdateStudentsData(spreadSheetService, updatedStudentsData)


if __name__ == "__main__":
    main()