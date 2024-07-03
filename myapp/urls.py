from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('Logout/', views.logout_page, name='Logout_page'),
    path('Register/', views.register_page, name='Register'),
    path('Insert/', views.Insert_page, name='Insert'),
    path('Display/', views.Display_page, name='Display'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('kanji/<str:level>', views.kanji_list, name='kanji_list'),
    path('test/', views.test_list, name='test'),
]
