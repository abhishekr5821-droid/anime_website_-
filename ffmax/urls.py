from django.urls import path
from . import views
from ffmax import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),   # ✅ THIS LINE
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout'),  # if you have logout
    

    path('service/', views.service, name='service'),
    path('webdevelopment/', views.webdevelopment, name='webdevelopment'),
    path('graphicdesign/', views.graphicdesign, name='graphicdesign'),
    path('anime/', views.anime, name='anime'),
    path('search/', views.search, name='search'),
]