
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
   path("", home_view, name="home"),
   path("draft", draft_post, name="draft"),
   path("archive", archive_post, name="archive"),
   path("my-post", user_post, name="pub_post"),
   path("posts", post_list_view, name="blog-home"),
   path("posts/new/", post_create_view, name="post_create"),
   path("posts/<int:pk>/<slug:slug>/", post_detail_view, name="post_detail"),
   path("posts/<int:pk>/<slug:slug>/update", post_update_view, name="post_update"),
   path("posts/<int:pk>/<slug:slug>/delete", post_delete_view, name="post_delete"),
 

]
