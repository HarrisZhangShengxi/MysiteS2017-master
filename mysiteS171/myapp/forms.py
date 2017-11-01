from django import forms
from models import Announcement, User
from django.contrib.auth.forms import UserCreationForm
# class AnnouncementForm(forms.ModelForm):
#     class Meta:
#         model=Announcement
#         fields=['title','description','date']
#         widget={'date':forms.RadioSelect()}
#         label={'date':('Preferred Time'),'avg_age':('What is your age?'),'intro_course':('This should be an introductory level course')}


class Project_EstaForm(forms.Form):
    no = no
class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect(), choices=((1, 'Yes'), (0, 'No')))
    age = forms.IntegerField(initial='20')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Additional Comments')

class ManagerForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name','last_name','position','phone']

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields=['username','first_name','last_name','email','position','phone']