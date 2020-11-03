from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("item/create", views.createItem),
    path("items/<itemid>", views.showItem),
    path("addToFavorite/<itemid>", views.addUserToItem),
    path("items/<itemid>/destroy", views.deleteItem),
    path("items/<itemid>/edit", views.editItem),
    path("items/<itemid>/update", views.updateItem)
]
