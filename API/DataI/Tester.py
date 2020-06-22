import json

from xlsxwriter.exceptions import FileCreateError

from DataI.Controllers.FileLoaders.CSVFileLoader import CSVFileLoader
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader
from DataI.Controllers.FileSaver.CSVFileSaver import CSVFileSaver
from DataI.Controllers.FileSaver.ExcelFileSaver import ExcelFileSaver
from DataI.Controllers.FileSaver.FileSaver import FileSaver
from DataI.JSONSerializer import ObjectEncoder

xl = ExcelFileLoader(r'C:\Users\Allonios\Desktop\Project 1\Test.xlsx')
tablesList = xl.loadFile(0)
jsonString = json.dumps(tablesList, indent=4, cls=ObjectEncoder, ensure_ascii=False)
fHandler = open('openXLTester.json', 'w', encoding='utf8')
fHandler.write(jsonString)

# csv = CSVFileLoader(r'C:\Users\Allonios\Desktop\Project 1\Test.csv')
# table = csv.loadFile(0)
# print(FileSaver.tableToDataFrameConverter(table))
# jsonString = json.dumps(table, indent=4, cls=ObjectEncoder, ensure_ascii=False)
# fHandler = open('openCSVTester.json', 'w', encoding='utf8')
# fHandler.write(jsonString)

saver = CSVFileSaver('demo.csv')
try:
    saver.saveFile(tablesList)
except FileCreateError:
    print('file is opened else where')

# import pandas as pd
#
# # dataframe Name and Age columns
# df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
#                    'Age': [10, 0, 30, 50]})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# df.to_excel(writer, sheet_name='Sheet2', index=False)
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()



