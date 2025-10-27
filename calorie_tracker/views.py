from django.shortcuts import render, redirect
from .models import FoodEntry

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        calories = request.POST.get("calories")
        if name and calories.isdigit():
            FoodEntry.objects.create(name=name, calories=int(calories))
        return redirect("home")

    entries = FoodEntry.objects.all().order_by("-id")
    total_calories = sum(entry.calories for entry in entries)
    return render(request, "index.html", { 
        "entries": entries,
        "total_calories": total_calories
    })

def remove_food(request, pk):
    FoodEntry.objects.filter(id=pk).delete()
    return redirect("home")

def reset_calories(request):
    FoodEntry.objects.all().delete()
    return redirect("home")
