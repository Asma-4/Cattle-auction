from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('add_cow',views.add_cow,name='add_cow'),
    path('list_cow',views.list_cow,name='list_cow'),
    path('contacts',views.contactPage,name='contacts'),
    path('delete/<str:pk>',views.deleteCow,name='delete'),
    path('update/<str:pk>',views.updateCow,name='update'),

    path('about',views.aboutPage,name='about'),
  
]