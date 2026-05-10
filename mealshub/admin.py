from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Student, Meal, Order

admin.site.register(Student)
admin.site.register(Meal)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'meal', 'week_number', 'day', 'view_orders')

    def day(self, obj):
        return obj.meal.get_day_display()

    def view_orders(self, obj):
        url = reverse('orders_list')
        return format_html('<a href="{}">View Orders Page</a>', url)

    view_orders.short_description = "Orders List"
