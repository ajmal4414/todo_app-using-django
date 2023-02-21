
from django.urls import path
from .views import Tasklist, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView
from .import views
urlpatterns =[
    path('task-list',Tasklist.as_view(),name='Tasks'),
    path('task-create',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(),name='task-detail'),
    path('login/',views.login_fun,name='login'),
    path('register/',views.register_fun,name='register')


]