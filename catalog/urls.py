from django.urls import path

from catalog.views import base, data, description

urlpatterns = [
    path('', base, name='base'),
    path('data/', data, name='data'),
    path('desc/<int:pk>', description, name='desc')
]