from django.urls import path
from . import views 


app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('edit/<slug:slug>/', views.post_edit, name='post-edit'),
    path('delete/<slug:slug>/', views.post_delete, name='post-delete'),
    path('<slug:slug>/', views.post_page, name='page'),
]
