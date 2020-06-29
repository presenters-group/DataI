from django.urls import path

from DataI import views

urlpatterns = [
  path('dataSourceTableWithoutXcolumn-sources/', views.dataSourcesHandler),
  path('dataSourceTableWithoutXcolumn-sources/<int:id>/', views.dataSourceModifier),
  path('visualizers/', views.visualizersHandler),
  path('visualizers/<int:id>/', views.visualizerModifier),
  path('dashboards/', views.dashBoardsHandler),
  path('dashboards/<int:id>/', views.dashboardModifier),
  path('filters/', views.filtersHandler),
  path('filters/<int:id>/', views.filterModifier),
  path('', views.fullDataHandler),

]
