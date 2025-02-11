from django.urls import path, include

from asset import views

urlpatterns = [
    # path("asset_list", views.asset_list, name="asset_list"),
    path("", views.top, name="top"),
    path("new_asset/", views.new_asset, name="new_asset"),
    path("asset_edit/<uuid:id>", views.asset_edit, name="asset_edit"),
    path("asset_detail/<uuid:id>", views.asset_detail, name="asset_detail"),
    path("asset_delete/<uuid:id>", views.asset_delete, name="asset_delete"),
    path("accounts/", include("accounts.urls")),
]
