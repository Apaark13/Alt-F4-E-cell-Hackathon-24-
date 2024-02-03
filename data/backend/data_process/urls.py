# yourappname/urls.py

from django.urls import path
from .views import process_and_store_data

urlpatterns = [
    path('process/', process_and_store_data, name='process_and_store_data'),
]
