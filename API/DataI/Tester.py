import os

from DataI.Controllers.DataControllers.DataController import DataController
from DataI.Controllers.FileLoaders.ExcelFileLoader import ExcelFileLoader


projectPath = os.path.dirname(__file__)
filePath = (os.path.join(projectPath.replace('/DataI', '')) + '/media/uploaded/') + 'Test.xlsx'

print(filePath)

loader1 = ExcelFileLoader(filePath)
tables1 = loader1.loadFile(0)
print(len(tables1))


dirName = os.path.dirname(__file__)
filename = os.path.join(dirName, '../Test.xlsx')
loader2 = ExcelFileLoader(filename)

tables2 = loader2.loadFile(DataController.getMaxIdInList(tables1))

tables1.extend(tables2)

print(len(tables1))
