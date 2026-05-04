from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/<int:week_number>/", views.menu_view, name="menu"),
    path('order/success/', views.order_success, name='order_success'),
    path('order/week/<int:week_number>/submit/', views.weekly_order_submit, name='weekly_order_submit'),
 ]
