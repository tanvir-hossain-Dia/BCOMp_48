from django.urls import path

from bootapp import views

urlpatterns = [
    path('p2/',views.mypage2,name='batas'),
    path('p3/',views.mypage3,name='patal'),

]