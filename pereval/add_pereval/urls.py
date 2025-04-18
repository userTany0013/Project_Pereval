from django.urls import path

from .views import submitData

urlpatterns = [
    path('submitData/', submitData.as_view(), name='pereval_add'),
    path('submitData/<id>/', submitData.as_view(), name='pereval_data'),
]
