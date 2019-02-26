from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.page2, name='page2'),
    path('', views.page3, name='page3'),
    path('', views.page4, name='page4'),
    path('', views.page5, name='page5'),

]