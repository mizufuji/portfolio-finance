from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ticker_name = models.CharField("ティッカー", max_length=20, null=True, blank=True)
    asset_name = models.CharField("資産名", max_length=100, null=False)
    quantity = models.FloatField("数量", null=False)
    price = models.FloatField("価格", null=False)
    asset_type = models.CharField("種類", max_length=50)
    company_name = models.CharField("会社名", max_length=100)
    buying_date = models.DateField("購入日")

    def __str__(self):
        return self.asset_name
