import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def Stablishes_connection():
    """
    Establishes connection with the Google Sheets API and returns the required spreadsheet service.

    Returns:
        spreadSheetService: The connected spreadsheet service.
    """

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = None

    if os.path.exists("sheetsManagment/token.json"):
        creds = Credentials.from_authorized_user_file("sheetsManagment/token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "sheetsManagment/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("sheetsManagment/token.json", "w") as token:
            token.write(creds.to_json())

    service = build("sheets", "v4", credentials=creds)

    print("Connection succesful")

    return service