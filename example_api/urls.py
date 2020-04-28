from django.urls import path
from .views import *

urlpatterns = [
  path('', ConnectListView.as_view()),
  path('news/', NewsView.as_view()),
  path('greenfield/', GreenfieldViews.as_view()),
  path('support/', SupportView.as_view()),
  path('news/detail/<slug:pk>', DetailNews.as_view()),
  path('all_news/', Allnews.as_view()),
  path('support/detail/<int:pk>', DetailSupport.as_view())
]
