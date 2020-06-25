from django.urls import path

from DataI import views

urlpatterns = [
  path('data-sources/', views.dataSourcesHandler),
  path('data-sources/<int:id>/', views.dataSourceModifier),
  path('data-sources/cell/<int:tableId>/<int:columnId>/<int:cellIndex>/', views.cellModifier),
  path('visualizers/', views.visualizersHandler),
  path('visualizers/<int:id>/', views.visualizerModifier),
  path('dashboards/', views.dashBoardsHandler),
  path('dashboards/<int:id>/', views.dashboardModifier),
  path('filters/', views.filtersHandler),
  path('filters/<int:id>/', views.filterModifier),
  path('chartsNames/', views.getChartsNames),
  path('excel-upload/', views.excelUpload),
  path('csv-upload/', views.csvUpload),
  path('', views.fullDataHandler),

]
