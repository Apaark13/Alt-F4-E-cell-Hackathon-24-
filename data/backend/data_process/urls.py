# yourappname/urls.py

from django.urls import path
from .views import process_and_store_data
app_name = 'data_process'
urlpatterns = [
    path('process_and_store_data/', process_and_store_data, name='process_and_store_data'),
    # ... other URL patterns
]
