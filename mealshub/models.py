from django.db import models

# Create your models here.
CLASS_CHOICES = [
    ('Class 1', 'Class 1'),
    ('Class 2', 'Class 2'),
    ('Class 3', 'Class 3'),
    ('Class 4', 'Class 4'),
]

WEEK_CHOICES = [
    (1, 'Week 1'),
    (2, 'Week 2'),
    (3, 'Week 3'),
]

DAY_CHOICES = [
    ('Mon', 'Monday'),
    ('Tue', 'Tueday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
]

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    allergies = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.class_name})"


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    week = models.IntegerField(choices=WEEK_CHOICES)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)

    def __str__(self):
        return f"{self.name} (Week {self.week} {self.get_day_display()})"


class Order(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} ordered {self.meal} on {self.date}"
