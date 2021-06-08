from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage,name='main'),
    path('quizpanel/',views.panel,name='panel'),
    path('beginner/',views.beginner,name='beginner'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('aboutus/',views.aboutus,name='Aboutus')

]