from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/<int:week_number>/", views.menu_view, name="menu"),
    path('order/<int:meal_id>/', views.order_meal, name='order_meal'),
    path('order/success/', views.order_success, name='order_success'),
]
