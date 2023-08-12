from django.urls import path
from .import views

app_name='items'

urlpatterns=[
    path('home/',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('front_page/',views.front_page,name='front_page'),
    path('new/',views.new,name='new'),
    path('<int:id>/',views.detail,name='detail'),
    path('search_value/',views.search_value,name='search_value'),
]