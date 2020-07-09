from DataI.Controllers.Filters.FilterController import MultipleEqualityFilter, NumericFilter


class FiltersFactory():
    @classmethod
    def getFilter(cls, filterType: str):
        if filterType == 'MultipleEquality':
            return MultipleEqualityFilter()
        else:
            return NumericFilter()
