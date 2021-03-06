from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.ArticleList.as_view()),
    path("write/", views.ArticleAdd.as_view()),
    path("<int:pk>/write/", views.ArticleDetail.as_view()),
    path("<int:pk>/write/put", views.ArticleMod.as_view()),
    path("<int:pk>/write/delete", views.ArticleDel.as_view()),
    path("comment/write/", views.CommentList.as_view()),
    path("comment/<int:pk>/write/put", views.CommentMod.as_view()),
    path("comment/<int:pk>/write/delete", views.CommentDel.as_view()),
    path("<int:pk>/suggestion/", views.ArticleLikesDetail.as_view()),
    path("comment/<int:pk>/suggestion/", views.CommentLikesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
