from django.urls import path

from apps.product.views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('detail/<int:pk>/', ProductDetailView.as_view()),
    path('update/<int:pk>/', ProductUpdateView.as_view()),
    path('delete/<int:pk>/', ProductDeleteView.as_view()),

]
