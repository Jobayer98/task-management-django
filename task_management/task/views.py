from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task

class SignUpView(CreateView):
    template_name = 'task/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response

class LoginView(TemplateView):
    template_name = 'task/login.html'

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        return self.render_to_response({'form': form})

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
    