from django.urls import path
from .views import *
urlpatterns = [
    path('', EventViews.as_view()),
    path('winners/<int:pk>', WinnersView.as_view())
]