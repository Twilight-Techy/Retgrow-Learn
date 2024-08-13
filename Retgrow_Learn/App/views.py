from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Course, Task

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if any of the fields are missing
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('home')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('home')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('home')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect('home')

    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if any of the fields are missing
        if not username or not password:
            messages.error(request, "All fields are required.")
            return redirect('home')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')

    return redirect('home')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def home_view(request):
    return render(request, 'index.html')


def learning_paths_view(request):
    courses = Course.objects.all()  # You might want to group these into categories
    return render(request, 'learning_paths.html', {'courses': courses})


def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    levels = course.levels.prefetch_related('modules__tasks')

    structured_content = []

    for level in levels:
        level_content = {
            "level_name": level.name,
            "modules": []
        }
        for module in level.modules.all():
            module_content = {
                "module_name": module.name,
                "tasks": []
            }
            for task in module.tasks.all():
                task_content = {
                    "task_name": task.name,
                    "description": task.description,
                    "link": task.link,
                    "link_name": task.link_name,
                }
                module_content["tasks"].append(task_content)
            level_content["modules"].append(module_content)
        structured_content.append(level_content)

    context = {
        'course': course,
        'structured_content': structured_content,
    }

    return render(request, 'course_details.html', context)

def resources_view(request):
    # This view will handle the resources page
    # You might want to add a Resources model if you have structured data
    return render(request, 'resources.html')