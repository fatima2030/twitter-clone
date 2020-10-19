from django.urls import path

from .views import (PostListView,
FollowsListView,FollowersListView,
PostCreateView,UserPostListView,
PostDeleteView,PostDetailView,
PostOpdateView,PostPreference,
SearchView,UserProfile,

)


urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('UserProfile',UserProfile.as_view(),name='UserProfile'),

    path('user/<str:username>/follows',FollowsListView.as_view(),name='user-follows'),
    path('user/<str:username>/followers',FollowersListView.as_view(),name='user-followers'),
    path('post/new',PostCreateView.as_view(),name='post-create'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/del',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostOpdateView.as_view(),name='post-update'),
    path('post/<int:postid>/preference/<int:userpreference>',PostPreference,name='postpreference'),


    path('search/', SearchView, name='search'),









]