from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/', BlogListView.as_view(), name='list'),
    path('blog/<int:pk>/view/', BlogDetailView.as_view(), name='view'),
    path('blog<int:pk>edit/', BlogUpdateView.as_view(), name='edit'),
    path('blog<int:pk>delete/', BlogDeleteView.as_view(), name='delete'),
]