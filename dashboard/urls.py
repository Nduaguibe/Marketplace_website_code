from django.urls import path
from .import views

app_name = 'dashboard'

urlpatterns = [
    path('<id>/book_view',views.book_view,name='book_view'),
    path('phone_view/',views.phone_view,name='phone_view'),
    path('toy_view/',views.toy_view,name='toy_view'),

]