from django.urls import path
from login.views import showpage,UserCreateView, show

urlpatterns = [
        path('', UserCreateView.as_view(), name='auth'),
        path('test/', show, name='test'),
        ]
