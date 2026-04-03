from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def dashboard(request):
    # This will be the main page users see after they log in
    return render(request, 'tasks/dashboard.html')

# Create your views here.
def my_tasks(request):
    # This will load a new page specifically for tasks
    return render(request, 'tasks/my_tasks.html')