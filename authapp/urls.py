from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('', authapp.index, name='index'),
    path('signin/', authapp.UserLoginView.as_view(), {'pagemode': 'signin'}, name='signin'),
    path('signup/', authapp.UserLoginView.as_view(), {'pagemode': 'signup'}, name='signup'),
]