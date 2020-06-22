from django.urls import path

from DataI import views

urlpatterns = [
    path('', views.getStaticData, name='static-data'),
    path('<int:question_id>/', views.modStaticData, name='mod-static-data'),
]