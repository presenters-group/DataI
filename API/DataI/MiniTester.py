from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel
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

cell1 = CellModel(10, enums.CellType.numeric.value)
cell2 = CellModel(-5, enums.CellType.numeric.value)

print(cell1 + cell2)
print(cell2 + cell1)


import datetime
import re

from dateutil.parser import parse

from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel

date1 = '22/1/2000'
date2 = '2000-01-22 00:00:00'


try:
    dateObj1 = parse(date1, fuzzy=False)
    print(dateObj1)
    print(date2[:4])
except ValueError:
    print('not date')



















