from django.shortcuts import render, redirect, get_object_or_404

from asset.models import Asset

from django.contrib.auth.decorators import login_required
from asset.forms import AssetForm
import pandas
import yfinance as yf
import io
import urllib
import base64

# import pandas_datareader
import matplotlib.pyplot as plt
import japanize_matplotlib


# トップページ
@login_required
def top(request):
    assets = Asset.objects.filter(user=request.user)

    ticker_list = []
    for asset in assets:
        ticker = yf.Ticker(asset.ticker_name)
        ticker_list.append(ticker)

    plt.figure(figsize=(12, 4.8))

    for asset, ticker_asset in zip(assets, ticker_list):
        df = ticker_asset.history(period="1mo")
        df = df / df.iloc[0] * 100

        if not df.empty:
            plt.plot(df.index, df["Close"], label=asset.asset_name)
            # plt.plot(df.index, df["Close"], label=asset.ticker_name)
            # df = df / df.iloc[0] * 100

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Your Asset Price")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.getvalue()).decode("utf-8")
    uri = "data:image/png;base64," + string
    plt.close()

    context = {"assets": assets, "graph": uri}
    return render(request, "assets/top.html", context)


# Create処理
@login_required
def new_asset(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            # return redirect(asset_list, asset_id=asset.id)
            # return redirect("top", asset_id=asset.id)
            return redirect("top")
    else:
        form = AssetForm()

    return render(request, "assets/new_asset.html", {"form": form})


# Read処理
@login_required
def asset_detail(request, id):
    asset = get_object_or_404(Asset, id=id)
    print(asset)
    ticker = yf.Ticker(asset.ticker_name)
    print(asset.ticker_name)

    latest_close_rate = ticker.history(period="1d")["Close"].iloc[-1]
    latest_close_rate = float(f"{latest_close_rate:.2f}")
    total_price = asset.price * asset.quantity
    total_now_price = latest_close_rate * asset.quantity
    profit_loss = f"{total_now_price - total_price:.0f}"
    profit_loss = float(profit_loss)

    df = ticker.history(period="1mo")

    plt.figure(figsize=(12, 4.8))
    plt.plot(df.index, df["Close"], label="Close Price", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"Price Trend: {asset.ticker_name}")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.getvalue()).decode("utf-8")
    uri = "data:image/png;base64," + string
    plt.close()

    return render(
        request,
        "assets/asset_detail.html",
        {
            "asset": asset,
            "latest_close_rate": latest_close_rate,
            "total_price": total_price,
            "total_now_price": total_now_price,
            "profit_loss": profit_loss,
            "graph": uri,
        },
    )


# Update処理
@login_required
def asset_edit(request, id):
    asset = get_object_or_404(Asset, pk=id)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect("top")
    else:
        form = AssetForm(instance=asset)
    return render(request, "assets/asset_edit.html", {"form": form})


# Delete処理
@login_required
def asset_delete(request, id):
    if request.method == "POST":
        asset = get_object_or_404(Asset, id=id)
        asset.delete()
        return redirect("top")

    return redirect("asset_detail", id=id)
