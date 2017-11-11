from django import forms
from models import Announcement, Employee, Issue, Answer, Project
from django.contrib.auth.forms import UserCreationForm

class AnnouncementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=10000)
    author = forms.CharField(label='Author', max_length=50)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class RequirementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=10000)
    costumer = forms.CharField(label='Costumer', max_length=50)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class IssuesForm(forms.Form):
    object = forms.CharField(label='Object', widget=forms.Textarea)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class SolutionForm(forms.Form):
    add_solution = forms.CharField(label='Add Solution', widget=forms.Textarea)

class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect(), choices=((1, 'Yes'), (0, 'No')))
    age = forms.IntegerField(initial='20')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Additional Comments')

class UserForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','position','phone']

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Employee
        fields=['username','first_name','last_name','email','position','phone']

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = ['project_no','name','leader','start_data','end_date','phase','description']