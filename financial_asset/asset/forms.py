from django import forms

from asset.models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = (
            "asset_name",
            "ticker_name",
            "quantity",
            "price",
            "asset_type",
            "company_name",
            "buying_date",
        )
        help_texts = {
            "ticker_name": "※日本株の場合はティッカーシンボルの後に.Tをつけてください。"
        }
