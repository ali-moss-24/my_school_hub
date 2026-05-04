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


# Sucess page
def order_success(request):
    return render(request, 'mealshub/order_success.html')

# Weekly order
def weekly_order_submit(request, week_number):
    if request.method == 'POST':
        
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Validate meals FIRST (so error shows if name is missing)  
        for day in days:
            selected = request.POST.getlist(f"meal_{day}")
            if len(selected) > 1:
                messages.error(request, f"Please select only ONE meal for the {day}.")
                return redirect('menu', week_number=week_number)

# Now validate student name
        student = request.POST.get('student')
        if not student:
            messages.error(request, "Please enter the student name.")
            return redirect('menu', week_number=week_number)

            
# Create orders (one per day)
        for day in days:
            if len(selected) == 1:
                meal = Meal.objects.get(id=selected[0])
                Order.objects.create(
                    student=student,
                    meal=meal,
                    date=meal.date
                )

        return redirect('order_success')
    return redirect('menu', week_number=week_number)
