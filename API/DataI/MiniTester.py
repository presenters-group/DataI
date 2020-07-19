# from DataI import enums
# from DataI.Models.ColumnModel import CellModel, ColumnModel
#
# cells1 = [CellModel('السعر', enums.CellType.string.value),
#         CellModel(10, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(20, enums.CellType.numeric.value),
#         CellModel(15, enums.CellType.numeric.value),
#         CellModel(15, enums.CellType.numeric.value),
#         CellModel(10, enums.CellType.numeric.value),
#         CellModel(10, enums.CellType.numeric.value)
#          ]
#
# cells2 = [CellModel('Col2', enums.CellType.string.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value),
#         CellModel(2, enums.CellType.numeric.value)
#          ]
#
# col1 = ColumnModel(cells1, 'السعر', 0, False)
# col2 = ColumnModel(cells2, 'Col2', 1, False)
#
# col = '0' / col1
#
# cell1 = CellModel(7, enums.CellType.numeric.value)
# cell2 = CellModel(2, enums.CellType.numeric.value)
#
#
#
# for cell in col.cells:
#         print(cell)
import datetime
from dateutil.parser import parse

from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel

date1 = '22/1/2000'
date2 = '23/1/2000'

try:
    dateObj1 = parse(date1, fuzzy=False)
    dateObj2 = parse(date1, fuzzy=False)
    print(date1 < date2)
except ValueError:
    print('not date')


























