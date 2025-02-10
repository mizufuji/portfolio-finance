from django import forms

from asset.models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = (
            "asset_name",
            "quantity",
            "price",
            "asset_type",
            "company_name",
            "buying_date",
        )
