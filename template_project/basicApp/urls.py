from django.urls import path
from basicApp import views
# TEMPLATE TEGGING
# To use it in the calling of the url
app_name = 'basic_app'




urlpatterns = [
    path('index/', views.index ,name='index'),
    path('basic/', views.basic ,name='basic'),
    path('other/', views.other ,name='other'),
    path('relative/', views.relative ,name='relative'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
