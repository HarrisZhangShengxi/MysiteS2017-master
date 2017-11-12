from django.shortcuts import render,render_to_response

from .models import Announcement, Task, Project, Answer, Issue, Requirement
from .forms import SolutionForm,ProjectForm, AnnouncementForm,RequirementForm,IssuesForm,InterestForm,RegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def base(request):
    return render(request,'management/base.html')

def IndexView(request):
    acmt_list = Announcement.objects.all()
    remt_list = Requirement.objects.all()
    return render(request,'management/index.html',{'acmtlist':acmt_list, 'remtlist':remt_list})

def AddProject(request):
    #topiclist = Project.objects.all()
    #if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save(commit=False)
            #topic.num_responses = 1
        project.save()
            #return HttpResponseRedirect(reverse('management:'))

    return render(request, 'management/addprojects.html',{'form':form})

def Project_list(request):
    Project_list = Project.objects.all()[:10]
    return render(request, 'management/projects_list.html', {'Project_list': Project_list})

def Issues_Detail(request):
    issue = Issue.objects.all()
    answer = Issue.objects.values_list("object", flat=True)
    return render(request, 'management/issues.html', {'issue':issue, 'solution':answer})


def Issues_list(request):
    issue_list = Issue.objects.all()
    return render(request, 'management/issues_list.html', {'issuelist':issue_list})


def Solution(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.num_responses = 1
            solution.save()
            return HttpResponseRedirect(reverse('management:solutions'))
    else:
        form = SolutionForm()
    return render(request, 'management/solutions.html', {'form':form})


def Profiles(request):
    profiles_info = Profiles.objects.all()[:10]
    return render(request, 'management/profiles.html', {'profiles_info': profiles_info})

def AddAnRe(request):
    if request.method == 'POST':
        Aform = AnnouncementForm(request.POST)
        if Aform.is_valid():
            announcement = Aform.save(commit=False)
            announcement.num_responses = 1
            announcement.save()
            return HttpResponseRedirect(reverse('management:index'))
        else:
            Aform = AnnouncementForm()

        Rform = RequirementForm(request.POST)
        if Rform.is_valid():
            requirement = Rform.save(commit=False)
            requirement.num_responses = 1
            requirement.save()
            return HttpResponseRedirect(reverse('management:index'))
        else:
            Rform = RequirementForm()
        return render(request, 'management/index.html', {'Aform':Aform, 'Rform':Rform})



def AddIssues(request):
    if request.method == 'POST':
        form = IssuesForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.num_responses = 1
            issue.save()
            return HttpResponseRedirect(reverse('management:issues_list'))
        else:
            form = IssuesForm()
        return render(request, 'management/issues_list.html', {'form': form})



#def topicdetail(request, topic_id):
#    topic = Topic.objects.filter(id=topic_id)
#    if request.method == 'POST':
#        form = InterestForm(request.POST)
#        if form.is_valid() and request.POST.get('interested') == '1':
#            interested = form.cleaned_data['interested']
#            age = form.cleaned_data['age']
#            for t in topic:
#                n = t.num_responses + 1
#                topic.update(num_responses=n)
#                a = (t.avg_age * t.num_responses + int(request.POST.get('age'))) / n
#                topic.update(avg_age=a)
#            return HttpResponseRedirect(reverse('myapp:topics'))
#        else:
#            return HttpResponseRedirect(reverse('myapp:topics'))
#    elif request.method == 'GET':
#        form = InterestForm()
#    return render(request, 'myapp/topicdetail.html', {'form': form, 'topic': topic})

def register(request):
    employeelist = Employee.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html',{'form':form, 'employeelist':employeelist})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))

#def mycourses(request):
 #   courses = Course.objects.filter(students__username=request.user.username)
  #  return render(request, 'myapp/mycourses.html', {'courses': courses})