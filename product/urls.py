from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
]




