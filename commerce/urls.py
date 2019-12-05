from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from commerce import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'commerces', views.CommerceViewSet)
router.register(r'commercesAddresse', views.CommerceAddressViewSet)
router.register(r'rewards', views.RewardViewSet)
router.register(r'rewardsDetail', views.RewardDetailViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
