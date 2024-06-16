from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path('like/<int:book_id>/', like_book, name='like_book'),
    path("comment/<int:book_id>/", comment_book, name="comment_book"),
    path("create/", create, name="create_book"),
    path("edit/<int:book_id>", edit, name="edit_book"),
    path("delete/<int:id>", delete, name="delete_book"),
    path("detail/<int:book_id>/", card_detail, name="card_detail"),
]