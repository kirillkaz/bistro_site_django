from django.urls import path
from main_app.views import LoadMainPage, LoadAddProdPage, LoadLookProdPage
urlpatterns = [
        path('', LoadMainPage, name='main_page'),
        path('add/product', LoadAddProdPage, name='add_prod'),
        path('look/product', LoadLookProdPage, name='look_prod'),
        ]
