from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('addTodo/', views.addTodo),
    path('deleteTodo/<int:task_id>', views.deleteTodo),
    path('results/', views.search, name='search'),
]
