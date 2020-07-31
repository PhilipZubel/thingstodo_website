from django import forms
from .models import Task
 
 
class TaskForm(forms.ModelForm):
	#user = forms.CharField(initial= request.user)
    class Meta:
        model = Task
        fields = ['description', 'date']


