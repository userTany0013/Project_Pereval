from django.urls import path

from .views import submitData

urlpatterns = [
    path('add/', submitData.as_view(), name='pereval_add'),
]
