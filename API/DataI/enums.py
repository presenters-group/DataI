import enum

class ColumnDataType(enum.Enum):
    Dimensions = 'Dimensions'
    Measures = 'Measures'
    DateTime = 'DateTime'


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
    DateTime = 'DateTime'


class ChartTypes(enum.Enum):
    table = 'table'
    VerticalBarChart = 'VerticalBarChart'
    horizontalBarChart = 'horizontalBarChart'
    StackedBarChart = 'StackedBarChart'
    BasicLineChart = 'BasicLineChart'
    PointChart = 'PointChart'
    BoundaryLineChart = 'BoundaryLineChart'
    LineChart = 'LineChart'
    DoughnutChart = 'DoughnutChart'
    PieChart = 'PieChart'
    MultiplePieChart = 'MultiplePieChart'
    SmartPieChart = 'SmartPieChart'
    PyramidalChart = 'PyramidalChart'
    ManInfChart = 'ManInfChart'
    FemaleAndMaleChart = 'FemaleAndMaleChart'
    FemaleInfChart = 'FemaleInfChart'
    HealthyFoodChart = 'HealthyFoodChart'
    MapChart = 'MapChart'
    MapChartByLatitudeAndLongitude = 'GeometryMapChart'


class AggregationType(enum.Enum):
    BasicSum = 'BasicSum'
    BasicAvg = 'BasicAvg'

    DayBasedSum = 'DayBasedSum'
    DayBasedAvg = 'DayBasedAvg'

    MonthBasedSum = 'MonthBasedSum'
    MonthBasedAvg = 'MonthBasedAvg'

    YearBasedSum = 'YearBasedSum'
    YearBasedAvg = 'YearBasedAvg'



























