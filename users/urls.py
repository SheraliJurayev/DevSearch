from django.urls import path
from .views import profiles , userProfile , \
      loginUser , logoutUser ,\
        registerUser, userAccount,\
            editAccount, createSkill,\
                updateSkill


urlpatterns = [
    path('login/' , loginUser , name='login'),
    path('logout/' , logoutUser , name='logout'),   
    path('register/' , registerUser , name='register'),
    path('' , profiles , name = 'profiles') , 
    path('profile/<str:pk>/' , userProfile , name = 'user-profile') , 
    path('account/' , userAccount , name = 'account') , 
    path('edit-account/' , editAccount , name = 'edit-account') , 
    path('create-skill/' , createSkill , name = 'create-skill') , 
    path('update-skill/<str:pk>/' , updateSkill , name = 'update-skill') , 
]