from django.urls import path

from asset import views

urlpatterns = [
    # path("asset_list", views.asset_list, name="asset_list"),
    path("", views.top, name="top"),
    path("new_asset/", views.new_asset, name="new_asset"),
    path("asset_edit/<uuid:id>", views.asset_edit, name="asset_edit"),
]
