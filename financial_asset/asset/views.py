from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from asset.models import Asset

from django.contrib.auth.decorators import login_required
from asset.forms import AssetForm


def top(request):
    assets = Asset.objects.all()
    context = {"assets": assets}
    return render(request, "assets/top.html", context)


"""
def asset_list(request):
    return HttpResponse("資産リスト")
"""


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


"""
@login_required
def asset_delete(request, id):
    if request.method == "DELETE":
"""
