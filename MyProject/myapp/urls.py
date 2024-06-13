from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path('like/<int:clothing_id>/', like_book, name='like_book'),
    path("comment/<int:clothing_id>/", comment_book, name="comment_book"),
    path("create/", create, name="create_book"),
    path("edit/<int:id>", edit, name="edit_book"),
    path("delete/<int:id>", delete, name="delete_book"),
    path("update/<int:id>", update, name="update_book"),
    path("view/<int:id>", read, name="view_book"),
    path("detail/<int:book_id>/", card_detail, name="card_detail"),
]