from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='blog-home'),
    path('blog/<int:id>/',views.BlogView,name='blog-detail'),
    path('create_blog/', views.CreateBlog, name='create-blog'),
    path('edit_blog/<int:id>/',views.EditBlog,name='edit-blog'),
    path('delete_blog/<int:id>/', views.DeleteBlog, name='delete-blog'),
]

