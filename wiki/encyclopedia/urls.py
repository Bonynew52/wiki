from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new"),
    path("random_page/", views.random_page, name="random"),
    path("edit_page/<str:title>/", views.edit_page, name="edit"),
    path("<str:title>/", views.entry, name="entry")
]
