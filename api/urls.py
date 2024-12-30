from django.urls import path

from api import views

urlpatterns = [
    # Products
    path("products/", views.ProductListAPIView.as_view()),
    path("products/info/", views.product_info),
    path("products/<int:pk>/", views.ProductDetailAPIView.as_view()),
    # Orders
    path("orders/", views.OrderListAPIView.as_view()),
]
