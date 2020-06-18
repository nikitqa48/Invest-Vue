from django.urls import path
from .views import *


urlpatterns = [
  path('', ConnectListView.as_view()),
  path('news/', NewsView.as_view()),
  path('greenfield/', GreenfieldViews.as_view()),
  path('support/', SupportView.as_view()),
  path('news/detail/<slug:pk>', DetailNews.as_view()),
  path('all_news/', Allnews.as_view()),
  path('support/detail/<int:pk>', DetailSupport.as_view()),
  path('document/<int:pk>', DocumentView.as_view()),
  path('project/<int:number>/', FilterProject.as_view()),
  path('project/<int:number>/<int:industry>/<int:year>', FilterProject.as_view()),
  path('project/<int:number>/<int:industry>', FilterProject.as_view()),
  path('summyear/<int:sum>/<int:year>',SumYear.as_view()),
  path('project/', ProjectView.as_view()),
  path('searchyear/<int:year>', SearchYearView.as_view()),
  path('searchyear/<int:year>/<int:industry>', SearchYearView.as_view())
]
