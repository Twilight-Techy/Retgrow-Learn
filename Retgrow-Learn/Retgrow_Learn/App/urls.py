from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('learning_paths/', views.learning_paths_view, name='learning_paths'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('resources/', views.resources_view, name='resources'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
