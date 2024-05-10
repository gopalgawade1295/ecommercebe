from django.urls import path
from . import views

urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('user/register/', views.userRegister, name='userregister'),
    path('user/profile/', views.getUserProfile, name='userprofile'),
    path('users/', views.getUsers, name='users'),
    path('products/', views.getProducts, name='products'),
    path('product/<str:pk>/', views.getProduct, name='product'),
    path('order/add/', views.addOrderItems, name='ordersadd'),
    path('order/myorders/', views.getMyOrders, name='myorders'),
    path('order/<str:pk>/pay/', views.updateOrderToPaid, name='pay')
]
