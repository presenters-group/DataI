from django.urls import path

from DataI import views

urlpatterns = [
  path('data-sources/', views.dataSourcesHandler),
  path('visualizers/', views.visualizersHandler),
  path('dashboards/', views.dashBoardsHandler),
  path('filters/', views.filtersHandler),
  path('', views.fullDataHandler),

]
