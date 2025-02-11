from django.urls import path
from frontent import views

urlpatterns = [
    path('',views.home,name='w.home'),
    path('shop/',views.shop,name='w.shop'),
    path('shop-detail/<int:id>/', views.detail, name='w.detail'),
    path('contact/',views.contact,name='w.contact'),
    path('cart/',views.cart,name='w.cart'),
    path('add-cart/<int:id>/',views.add_cart,name='w.add_cart'),
    path('remove-cart-all/<int:id>/',views.remove_cart_all,name='w.remove_cart_all'),
    path('remove-cart/<int:id>/',views.remove_cart,name='w.remove_cart'),
    path('checkout/',views.checkout,name='w.checkout'),

    path('ajax/', views.ajax, name='w.ajax'),
    path('process/', views.process_data, name='w.process_data'),
]

