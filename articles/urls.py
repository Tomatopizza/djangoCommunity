from django.urls import path
from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='articles_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(),
         name='articles_detail_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='likes_view'),
    path('<int:article_id>/bookmark/', views.BookmarkView.as_view(), name='bookmarks _view'),
]
