import operator

from DataI.Models.ColumnModel import ColumnModel, CellModel


class NumericFilterController():

    def implementFilter(self, column: ColumnModel, filterOperator: str, value) -> ColumnModel:
        operators = {
            '=': operator.eq,
            'is': operator.eq,
            '!=': operator.is_not,
            'is not': operator.is_not,
            '<=': operator.le,
            '<': operator.lt,
            '>=': operator.ge,
            '>': operator.gt,
        }

        filteredCells = list()

        for cell in column.cells[1:]:
            if operators[filterOperator](cell.value, value):
                filteredCells.append(cell)
            else:
                filteredCells.append(CellModel('', cell.type))

        return ColumnModel(filteredCells, column.name, column.id, column.isDeleted)

