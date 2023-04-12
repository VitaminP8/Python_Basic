"""
URL configuration for goal_tracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from userapp.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.index_view),
    path('category-list/', views.CategoryListView.as_view()),
    path('goal-list/', views.GoalListView.as_view()),
    path('goal-create/', views.GoalCreateView.as_view()),
    path('goal-delete/<int:pk>/', views.GoalDeleteView.as_view()),
    path('goal-update/<int:pk>/', views.GoalUpdateView.as_view()),
    path('goal-detail/<int:pk>/', views.GoalDetailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
