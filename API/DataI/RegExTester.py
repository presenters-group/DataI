from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnModel

cells1 = [CellModel('السعر', enums.CellType.string.value),
        CellModel(10, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(20, enums.CellType.numeric.value),
        CellModel(15, enums.CellType.numeric.value),
        CellModel(15, enums.CellType.numeric.value),
        CellModel(10, enums.CellType.numeric.value),
        CellModel(10, enums.CellType.numeric.value)
         ]

cells2 = [CellModel('Col2', enums.CellType.string.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value),
        CellModel(2, enums.CellType.numeric.value)
         ]

col1 = ColumnModel(cells1, 'السعر', 0, False)
col2 = ColumnModel(cells2, 'Col2', 1, False)

col = col1 / col2

cell1 = CellModel(2, enums.CellType.string.value)
cell2 = CellModel(2, enums.CellType.string.value)

print(cell1 + cell2)






# for cell in col.cells:
#     print(cell)
