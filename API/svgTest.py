from DataI import enums
from DataI.Models.ColumnModel import CellModel, ColumnStyleModel, ColumnModel
from DataI.Models.TableModel import PropertiesModel, TableModel, AggregationModel

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

cells2 = [CellModel('الكمية', enums.CellType.string.value),
        CellModel(40, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(60, enums.CellType.numeric.value),
        CellModel(50, enums.CellType.numeric.value),
        CellModel(40, enums.CellType.numeric.value)
         ]

cells3 = [CellModel('النوع', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Laptop', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Mouse', enums.CellType.string.value),
        CellModel('Keyboard', enums.CellType.string.value),
        CellModel('Keyboard', enums.CellType.string.value),
         ]

style1 = ColumnStyleModel('#26C485', 1.0, 1.0, 'Calibri')
style2 = ColumnStyleModel('#3066BE', 1.0, 1.0, 'Calibri')
style3 = ColumnStyleModel('#DBD56E', 1.0, 1.0, 'Calibri')


column1 = ColumnModel(cells1, cells1[0].value, 0, style1, False)
column2 = ColumnModel(cells2, cells2[0].value, 1, style2, False)
column3 = ColumnModel(cells3, cells3[0].value, 2, style3, False)

columns = [column1, column2, column3]

#=================================================================================================================
#=================================================================================================================

properties = PropertiesModel(enums.FileType.DataI.value, 50)

aggregator = AggregationModel([], 0, False)

dataSource = TableModel(columns, 'Table1', 0, properties, aggregator, False)

#=================================================================================================================
#=================================================================================================================

for column, i in (dataSource.columns, range(len(dataSource.columns))):
  for cell in column.cells:
    print(cell.value)




























