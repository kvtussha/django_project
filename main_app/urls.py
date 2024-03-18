from django.urls import path
from django.views.decorators.cache import cache_page

from main_app.views import (contacts, ProductDetailView, ProductsListView, PostListView,
                            PostDetailView, PostCreateView, PostDeleteView, PostUpdateView,
                            ProductCreateView, ProductDeleteView, ProductUpdateView, VersionDetailView,
                            VersionCreateView, VersionUpdateView)

app_name = 'main_app'

urlpatterns = [
    path('', cache_page(60)(ProductsListView.as_view()), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product-detail'),
    path('product/form/', ProductCreateView.as_view(), name='product-form'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product-edit'),

    path('posts/', cache_page(60)(PostListView.as_view()), name='post-list'),
    path('post/<int:pk>/', cache_page(60)(PostDetailView.as_view()), name='post-detail'),
    path('post/form/', PostCreateView.as_view(), name='post-form'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),

    path('version/<int:version_id>/', cache_page(60)(VersionDetailView.as_view()), name='version-detail'),
    path('version/form/', VersionCreateView.as_view(), name='version-form'),
    path('version/edit/<int:pk>/', VersionUpdateView.as_view(), name='version-edit'),
]
