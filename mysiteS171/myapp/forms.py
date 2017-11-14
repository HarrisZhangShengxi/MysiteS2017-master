from django import forms

from .models import Announcement, Requirement, Project, Issue, Member, Issue_Detail


from django.contrib.auth.forms import UserCreationForm

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"

  #  title = forms.CharField(label='Title', max_length=10000)
   # author = forms.CharField(label='Author', max_length=50)
   # description = forms.CharField(label='Description', widget=forms.Textarea)

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = "__all__"
    #title = forms.CharField(label='Title', max_length=10000)
    #costumer = forms.CharField(label='Costumer', max_length=50)
    #description = forms.CharField(label='Description', widget=forms.Textarea)

class IssuesForm(forms.ModelForm):
    #object_name = forms.CharField(label='Object', widget=forms.Textarea)
    #description = forms.CharField(label='Description', widget=forms.Textarea)
    class Meta:
        model = Issue
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_no','name','leader','start_date','end_date','phase','description']

class IssueDetailForm(forms.ModelForm):
    class Meta:
        model = Issue_Detail
        fields = "__all__"


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['project_no','first_name', 'last_name', 'email', 'phone']



