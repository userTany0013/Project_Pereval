from django.urls import path

from .views import submitData, submitData_filter

urlpatterns = [
    path('submitData/', submitData.as_view(), name='pereval_add'),
    path('submit/<int:pk>/', submitData.as_view(), name='pereval_data_or_update'),
    path('submitData/filter/', submitData_filter.as_view(), name='pereval_data_filter'),

]
