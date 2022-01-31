from django.urls import path
from .views import ReadingCreateApi, ReadingAggrApi

urlpatterns = [
    path('v1/reading', ReadingCreateApi.as_view()),
    path('v1/reading/aggr', ReadingAggrApi.as_view()),
]
