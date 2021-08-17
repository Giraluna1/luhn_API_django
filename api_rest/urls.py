from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.hello, name="getting"),
    re_path(r'(?P<number>[\w|\W]+)/$', views.franchise, name="credit card number")
]