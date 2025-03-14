# api/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('todos/', views.ToDoListCreate.as_view()),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete/', views.TodoToggleComplete.as_view()),  
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]