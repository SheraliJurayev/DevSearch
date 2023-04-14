from django.urls import path
from .views import profiles , userProfile , loginUser , logoutUser


urlpatterns = [
    path('login/' , loginUser , name='login'),
    path('logout/' , logoutUser , name='logout'),   
    path('' , profiles , name = 'profiles') , 
    path('profile/<str:pk>/' , userProfile , name = 'user-profile') , 
]