from django.contrib import admin
from django.urls import path, include

from asset.views import top

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", top, name="top"),
    path("financial_asset/", include("asset.urls")),
    path("accounts/", include("accounts.urls")),
]
