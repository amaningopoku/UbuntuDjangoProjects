from django.urls import path
from .views import index, user_details, add_user

app_name = 'userinfoapp'

urlpatterns = [
    path('', index, name='user_info'),
    path('<int:user_id>', user_details, name='user_details'),
    path('add_user', add_user, name='add_user')
]