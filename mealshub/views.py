from django.shortcuts import render
from .models import Meal


def home(request):
    return render(request, 'index.html')


def menu_view(request, week_number):
    meals = Meal.objects.filter(week=week_number, is_available=True).order_by('day', 'name')

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
