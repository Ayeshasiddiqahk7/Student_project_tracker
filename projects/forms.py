from django import forms
from .models import Project, Student

class ProjectForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'students']

