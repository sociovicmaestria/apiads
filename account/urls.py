from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from account import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'exchanges', views.ExchangeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
