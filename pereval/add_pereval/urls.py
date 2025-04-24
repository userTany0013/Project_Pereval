from django.urls import path

from .views import submitData

urlpatterns = [
    path('submitData/', submitData.as_view(), name='pereval_add'),
    path('submitData/<int:pk>/', submitData.as_view(), name='pereval_data_or_update'),
#    path('submitData/?user__email=<email>/', submitData.as_view(), name='pereval_email_data')
]
