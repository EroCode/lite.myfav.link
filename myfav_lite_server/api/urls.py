from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'link', views.LinkEntryViewSet)
router.register(r'category', views.CategoryEntryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]