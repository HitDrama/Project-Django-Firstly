from django.urls import path
from system import views

urlpatterns = [
    path('manager/', views.manager, name='s.manager'),
    path('baotri/', views.config, name='s.config'),

    #url danh muc
    path('category/', views.category,name='s.category'),
    path('add_category/', views.add_category,name='s.add_category'),
    path('del_category/<int:id>/', views.del_category,name='s.del_category'),
    path('edit_category/<int:id>/', views.edit_category,name='s.edit_category'),

    #url san pham
    path('product/', views.product,name='s.product'),
    path('add_product/', views.add_product,name='s.add_product'),
    path('del_product/<int:id>/', views.del_product,name='s.del_product'),
    path('edit_product/<int:id>/', views.edit_product,name='s.edit_product'),

    #url account
    path('account/', views.account, name='s.account'),
    path('account/add', views.add_account, name='s.add_account'),
    path('del_account/<int:id>/', views.del_account, name='s.del_account'),
    path('edit_account/<int:id>/', views.edit_account, name='s.edit_account'),
]