from django.urls import include,path
from rest_framework import routers
from .import views
router=routers.DefaultRouter()
router.register(r'heroes',views.HeroViewSet)
# wire up our API using automatic URL routing
# addictionally ,we include login  URLS for the browsable API
urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
