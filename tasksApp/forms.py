from django.forms import ModelForm
from .models import Tasks

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        exclude = ["uuid"]