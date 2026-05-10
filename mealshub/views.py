from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Meal, Order


def home(request):
    return render(request, 'index.html')


def menu_view(request, week_number):
    meals = Meal.objects.filter(
        week=week_number,
        is_available=True
        ).order_by('day', 'name')


# Group meals by day
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    grouped = {day: [] for day in days}

    for meal in meals:
        grouped[meal.day].append(meal)

    context = {
        "week_number": week_number,
        "grouped_meals": grouped
    }

    return render(request, "mealshub/menu.html", context)


# Weekly order
def weekly_order_submit(request, week_number):
    if request.method == 'POST':

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

        # 1. VALIDATE STUDENT NAME
        student = request.POST.get('student', '').strip()
        if not student:
            messages.error(request, "Please enter the student's name.")
            return redirect('menu', week_number=week_number)
        
        # GET CLASS NAME
        class_name = request.POST.get('class_name')

        # 2. VALIDATE MEAL SELECTIONS
        selected_meals = []

        for day in days:
            selected = request.POST.getlist(f"meal_{day}")

            # More than one selected for a day → invalid
            if len(selected) > 1:
                messages.error(request, f"Please select only ONE meal for {day}.")
                return redirect('menu', week_number=week_number)

            # Exactly one selected → store it
            if len(selected) == 1:
                selected_meals.append(selected[0])

        # No meals selected at all → invalid
        if not selected_meals:
            messages.error(request, "Please select at least one meal for the week.")
            return redirect('menu', week_number=week_number)

        # 3. CREATE ORDERS
        for meal_id in selected_meals:
            meal = Meal.objects.get(id=meal_id)
            Order.objects.create(
                student=student,
                class_name=class_name,
                meal=meal,
                week_number=week_number
            )

        return redirect('order_success')

    # If GET request → redirect safely
    return redirect('menu', week_number=week_number)

# Success page
def order_success(request):
    return render(request, 'mealshub/order_success.html')

# Order List
def orders_list(request):
    day_filter = request.GET.get('day')
    orders = Order.objects.all()

    if day_filter:
        orders = orders.filter(meal__day=day_filter)

    totals = {
        "Mon": orders.filter(meal__day="Mon").count(),
        "Tue": orders.filter(meal__day="Tue").count(),
        "Wed": orders.filter(meal__day="Wed").count(),
        "Thu": orders.filter(meal__day="Thu").count(),
        "Fri": orders.filter(meal__day="Fri").count(),
    }

    context = {
        "orders": orders,
        "totals": totals
    }

    return render(request, "mealshub/orders_list.html", context)
