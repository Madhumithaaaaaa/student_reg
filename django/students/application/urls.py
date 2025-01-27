from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission')
]