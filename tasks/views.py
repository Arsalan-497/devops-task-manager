from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")

    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})


def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.completed = not task.completed
    task.save()

    return redirect("task_list")


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("task_list")


def health_check(request):
    return JsonResponse({"status": "ok"})