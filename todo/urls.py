from django.urls import path,include
from .views import dashboard, home, delete_todo,complete_todo

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('delete/<pk>', delete_todo, name="delete_todo"),
    path('complete/<pk>', complete_todo, name="complete_todo")

]
