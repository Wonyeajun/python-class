from django.urls import path, include
from account.views import * 

urlpatterns = [
    path('signup/', dummy_signup, name = 'dummy_signup'),
    path('login/', dummy_login, name = 'dummy_login'),
    path('logout/', dummy_logout, name = 'dummylogout')
    
]