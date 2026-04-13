from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('service/',views.service,name='service'),
    path('webdevelopment',views.webdevelopment,name='webdevelopment'),
    path('graphicdesign',views.graphicdesign,name='graphicdesign'),
    path('anime/',views.anime,name='anime'),
    path('signup_view/',views.signup_view,name='signup_view'),
    path('login/',views.login,name='login'),
]
