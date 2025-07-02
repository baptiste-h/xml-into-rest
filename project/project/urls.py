from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from orders.views import OrderViewset

router = routers.SimpleRouter()
router.register("order", OrderViewset, basename="order")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
