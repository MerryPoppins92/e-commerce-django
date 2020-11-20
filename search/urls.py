from django.urls import path

from .views import SearchProductView
    

app_name = 'instance'

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]