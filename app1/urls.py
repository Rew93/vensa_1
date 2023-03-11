from django.urls import path

from app1.views import index, rev

urlpatterns = [
    path('', index, name='index'),
    path('rev', rev, name='rev'),
]
