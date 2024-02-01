from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        # Handle search query
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

         # Filter by priority
        priority_filter = self.request.GET.get('priority', '')
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        # Filter by creation date
        created_at_filter = self.request.GET.get('created_at', '')
        if created_at_filter:
            queryset = queryset.filter(created_at=created_at_filter)

        # Filter by due date
        due_date_filter = self.request.GET.get('due_date', '')
        if due_date_filter:
            queryset = queryset.filter(due_date=due_date_filter)
            
        # Filter by is_complete
        is_complete_filter = self.request.GET.get('is_complete', '')
        print(is_complete_filter)
        if is_complete_filter:
            queryset = queryset.filter(is_complete=is_complete_filter)
            
        return queryset
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = 'task'

class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create_task.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy('task_list')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.success(request, ("Authentication failed, try again"))
            return redirect('login') 
    else:
        return render(request, 'authentication/login.html', {})

        
def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('task_list')
    else:
        return render(request, 'authentication/signup.html', {})


def index(request):
    return render(request, 'index.html', {})