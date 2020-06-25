import enum

class ColumnDataType(enum.Enum):
    Dimensions = 'Dimensions'
    Measures = 'Measures'


class FileType(enum.Enum):
    Excel = 'Excel'
    CSV = 'CSV'
    DataI = 'DataI'
    InvalidType = 'InvalidType'


class FilterType(enum.Enum):
    LessThan = 'LessThan'
    MoreThan = 'MoreThan'
    Equality = 'Equality'
    MultiLogic = 'MultiLogic'
    DimensionMultiLogic = 'DimensionMultiLogic'


class CellType(enum.Enum):
    string = 'string'
    numeric = 'numeric'


class ChartTypes(enum.Enum):
    table = 'table'
    verticalBarChart = 'verticalBarChart'
    horizontalBarChart = 'horizontalBarChart'
    StackedBarChart = 'StackedBarChart'
    BasicLineChart = 'BasicLineChart'
    PointChart = 'PointChart'
    BoundaryLineChart = 'BoundaryLineChart'
    DoughnutChart = 'DoughnutChart'
    PieChart = 'PieChart'


























