SPREADSHEET_ID = "1yEzMLGotflN5SiIhPbKo0yrngdiXystICWR2yfc_TQw"
SHEET_NAME = "engenharia_de_software!"
TOTAL_OF_CLASSES_RANGE_NAME = "engenharia_de_software!A2:H2"
UPDATE_RANGE_NAME = "engenharia_de_software!A4"
FIRST_STUDENT_ROW = 4


def ReadStudentsData(spreadSheetService) -> list:
    """
    Reads the students data from the spreadsheet and returns a list with this data.

    Args:
        spreadSheetService: The connected spreadsheet service.

    Returns:
        studentsData: A list containing the students data.
    """

    rowNumber: int = 4
    students: list = []
    newStudent: list = []
    sheet = spreadSheetService.spreadsheets()

    #It reads a new row from the sheet until the query returns an empty row
    while True:
        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=(SHEET_NAME +"A" + str(rowNumber) + ":F" + str(rowNumber)))
            .execute()
        )

        newStudent = result.get("values", [])
        print(newStudent)
        if newStudent != []:
            students.append(newStudent[0])
            rowNumber += 1
        else:
            break

    print("Values read:")
    print(students)

    return students


def UpdateStudentsData(spreadSheetService, updatedStudentsData: list):
    """
    Updates the students data in the spreadsheet with the updated data.

    Args:
        spreadSheetService: The connected spreadsheet service.
        updatedStudentsData: A list containing the updated students data.
    """

    sheet = spreadSheetService.spreadsheets()

    result = (
        sheet.values()
        .update(spreadsheetId=SPREADSHEET_ID,
                range=UPDATE_RANGE_NAME,
                valueInputOption="USER_ENTERED",
                body={"values": updatedStudentsData})
        .execute()
    )

    print("Updated Values:")
    print(updatedStudentsData)


def GetTotalNumberOfClasses(spreadSheetService) -> int:
    """
    Gets the total number of classes recorded in the spreadsheet.

    Args:
        spreadSheetService: The connected spreadsheet service.

    Returns:
        totalOfClasses: The total number of classes recorded.
    """

    sheet = spreadSheetService.spreadsheets()
    totalOfClasses: int

    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=TOTAL_OF_CLASSES_RANGE_NAME)
        .execute()
    )

    values = result.get("values", [])
    
    totalOfClasses = values[0][0].split()
    totalOfClasses = int(totalOfClasses[-1])
    print("Total of classes:", totalOfClasses)

    return totalOfClasses