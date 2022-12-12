import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scopes=[

    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds=ServiceAccountCredentials.from_json_keyfile_name("/home/amin/Documents/GitHub/Synchronizing-google-spreedshet-with-local-python-script/files/key.json",scopes=scopes)

files=gspread.authorize(creds)
workbook=files.open("Account_Mgt")
sheet=workbook.sheet1


# df = pd.DataFrame(sheet.get_all_records())
# usernames = df['user_name'].tolist()
# passwords = df['account_password'].tolist()

# # print(df)

# dataframe = pd.DataFrame(sheet.get_all_records())
# # print(dataframe)
# x=sheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
# # print (x)



# from gspread_dataframe import get_as_dataframe


# df = get_as_dataframe(sheet, parse_dates=True, usecols=[0,2])
# print(df)



user_name = sheet.col_values(1)
account_password = sheet.col_values(2)
for i in range(0,len(user_name)):
    print(user_name[i],":",account_password[i],"\n")

