from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter
router = SimpleRouter()
router.register('',ProfileListView)

urlpatterns = [
  path('inform/', inform_list),
  path('news/', news_list),
  path('greenfield/',green_list)
]
urlpatterns += router.urls