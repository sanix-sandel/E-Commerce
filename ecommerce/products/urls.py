from django.urls import path
from . import views

urlpatterns = [

    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/detail/<int:pk>', views.ProductDetailView.as_view(),
        name='product_detail'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(),
        name='product_delete'),
    path('product/update/<int:pk>', views.ProductUpdateView.as_view(),
        name='product_update'),        
]
