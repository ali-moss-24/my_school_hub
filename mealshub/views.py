from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal
from .forms import OrderForm


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


# Order a meal
def order_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.meal = meal
            order.save()
            return redirect('order_success')
        else:
            form = OrderForm()

        return render(
            request,
            'mealshub/order_meal.html',
            {'meal': meal, 'form': form}
        )


# Sucess page
def order_success(request):
    return render(request, 'mealshub/order_success.html')
