from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import *
from products.api.views import *
from orders.api.views import *

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename='users')
router.register("products", ProductViewSet, basename='products')
router.register("get_all_products", AllProductsViewSet, basename='get_all_products')

urlpatterns = [
    # Orders API links
    path('get_purchased_products', PurchasedProductsViewSet.as_view(), name="get_purchased_products"),
    path('purchase_product', PurchaseProductAPIView.as_view(), name="purchase_product"),
    path('get_total_revenue', GetTotalRevenueAPIView.as_view(), name="get_total_revenue"),

    path('signup', UserRegistrationAPIView.as_view(), name="list"),
    path('login', UserLoginAPIView.as_view(), name="login"),
    path('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
]

app_name = "api"

urlpatterns += router.urls
