from django.urls import path

from DataI import views

urlpatterns = [
    path('data-sources/', views.dataSourcesHandler),
    path('data-sources/<int:id>/', views.dataSourceModifier),
    path('data-sources/cell/<int:tableId>/<int:columnId>/<int:cellIndex>/', views.cellModifier),
    path('data-sources/column-color/<int:tableId>/<int:columnId>/', views.columnColorModifier),
    path('data-sources/row-color/<int:tableId>/<int:rowId>/', views.rowColorModifier),
    path('data-sources/insert-filter/<int:tableId>/', views.insertInDataSourceFilter),
    path('data-sources/update-filter/<int:tableId>/<int:filterId>/', views.updateInDataSourceFilter),
    path('data-sources/remove-filter/<int:tableId>/<int:filterId>/', views.removeInDataSourceFilter),

    path('visualizers/', views.visualizersHandler),
    path('visualizers/<int:id>/', views.visualizerModifier),
    path('visualizers/insert-filter/<int:visioId>/', views.insertInVisioFilter),
    path('visualizers/update-filter/<int:visioId>/<int:filterId>/', views.updateInVisioFilter),
    path('visualizers/remove-filter/<int:visioId>/<int:filterId>/', views.removeInVisioFilter),

    path('chartsNames/', views.getChartsNames),
    path('chart/', views.getChartSVG),

    path('dashboards/', views.dashBoardsHandler),
    path('dashboards/<int:id>/', views.dashboardModifier),
    path('dashboards/insert-filter/<int:dashboardId>/', views.insertInDashboardFilter),
    path('dashboards/update-filter/<int:dashboardId>/<int:visioId>/<int:filterId>/', views.updateInDashboardFilter),
    path('dashboards/remove-filter/<int:dashboardId>/<int:visioId>/<int:filterId>/', views.removeInDashboardFilter),
    path('dashboards/chart/<int:dashboardId>/<int:visioId>/', views.getDashboardVisioChart),
    path('dashboards/charts/<int:dashboardId>/', views.getAllDashboardCharts),

    path('filters/', views.filtersHandler),
    path('filters/<int:id>/', views.filterModifier),

    path('excel-upload/', views.excelUpload),
    path('csv-upload/', views.csvUpload),
        path('dataI-upload/', views.dataIUpload),
    path('svg-upload/', views.svgUpload),
    path('', views.fullDataHandler),
]
