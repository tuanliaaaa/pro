from django.urls import path
from . import views
urlpatterns = [
    path('index.html',views.index,name='home'),
    path('watches.html',views.watches,name='watch'),
    path('card.html',views.card,name='card'),
    path('card.html/<int:id>/',views.singerProduct,name='singerProduct'),
]