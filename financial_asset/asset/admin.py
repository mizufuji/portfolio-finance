from django.contrib import admin

# Register your models here.
from asset.models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "ticker_name",
        "asset_name",
        "quantity",
        "price",
        "asset_type",
        "company_name",
        "buying_date",
    )
