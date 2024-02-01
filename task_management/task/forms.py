from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ]
        model = Task
        fields = '__all__'
        widgets = {
            "user": forms.Select(attrs={"class": "bg-slate-50 border border-gray-300 my-3 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "title": forms.TextInput(attrs={"class": "bg-slate-50 border border-gray-300 my-3 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "Enter title"}),
            "description": forms.Textarea(attrs={"class": "bg-slate-50 border border-gray-300 my-3 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "Enter description", "rows": 4, "cols": 10}),
            "is_complete": forms.CheckboxInput(attrs={"class": "ms-2 text-sm my-3 font-medium text-gray-900 dark:text-gray-300"}),
            "priority": forms.Select(attrs={"class": "bg-slate-50 border border-gray-300 my-3 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            "due_date": forms.DateInput(attrs={"class": "bg-slate-50 border border-gray-300 my-3 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white", "type": "Date"})
        }