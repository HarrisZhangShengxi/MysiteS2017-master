from django import forms

from .models import Announcement, Requirement, User, Project, Task, Issue, Answer

from django.contrib.auth.forms import UserCreationForm

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'author', 'description']

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['title', 'customer', 'description']

class IssuesForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['object', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_no','name','leader','start_date','end_date','phase','description']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

# class InterestForm(forms.Form):
#     interested = forms.ChoiceField(widget=forms.RadioSelect(), choices=((1, 'Yes'), (0, 'No')))
#     age = forms.IntegerField(initial='20')
#     comments = forms.CharField(required=False, widget=forms.Textarea, label='Additional Comments')

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name','last_name','position','phone']

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields=['username','first_name','last_name','email']