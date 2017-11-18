from datetime import date
from django.contrib import messages
from django.shortcuts import render,render_to_response

from .models import Announcement, Requirement,  Project, Issue, Member, Issue_Detail
from .forms import ProjectForm, AnnouncementForm,RequirementForm,IssuesForm,MembersForm,IssueDetailForm,MemberRegisterForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    return render(request,'management/base.html')

def IndexView(request):
    acmt_list = Announcement.objects.all().order_by('-date')
    remt_list = Requirement.objects.all().order_by('-date')
    return render(request,'management/index.html',{'acmtlist': acmt_list, 'remtlist': remt_list})

def AddAnRe(request):
    Aform = AnnouncementForm(request.POST)
    if request.method == 'POST':
        if Aform.is_valid():
            announcement = Aform.save(commit=False)
            announcement.date = date.today()
            announcement.save()
            messages.add_message(request, messages.SUCCESS, 'You have been submitted successfully!')
            Aform = AnnouncementForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error! Please check your input again!')
            Aform = AnnouncementForm()
    else:
        Aform = AnnouncementForm()

    Rform = RequirementForm(request.POST)
    if request.method == 'POST':
        if Rform.is_valid():
            requirement = Rform.save(commit=False)
            requirement.date = date.today()
            requirement.save()
            messages.add_message(request, messages.SUCCESS, 'You have been submitted successfully!')
            Rform = RequirementForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error! Please check your input again!')
            Rform = RequirementForm()
    else:
        Rform = RequirementForm()

    return render(request, 'management/addindex.html', {'Aform': Aform, 'Rform': Rform})

def AddProject(request):
    form = ProjectForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            messages.add_message(request, messages.SUCCESS, 'You have been submitted successfully!')
            form = ProjectForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error! Please check your input again!')
            form = ProjectForm()
    else:
        form = ProjectForm()

    return render(request, 'management/addprojects.html', {'form': form})

def Project_list(request):
    if request.user.username == 'mica':
        Project_list = Project.objects.all()
    else:
        member = Member.objects.filter(first_name=request.user.username)
        Project_list = Project.objects.filter(members=member)
    return render(request, 'management/projects_list.html', {'Project_list': Project_list})

def AddIssues(request):
    form = IssuesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            issue = form.save(commit=False)
            issue.date = date.today()
            issue.save()
            messages.add_message(request, messages.SUCCESS, 'You have been submitted successfully!')
            form = IssuesForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error! Please check your input again!')
            form = IssuesForm()
    else:
        form = IssuesForm()
    return render(request, 'management/addissues.html', {'form': form})
    #issue = Issue.objects.all()
    #answer = Issue.objects.values_list("object", flat=True)
    #form = IssuesForm(request.POST)
    #if form.is_valid():
    #    issue = form.save(commit=False)
    #    issue.save()

    #return render(request, 'management/addissues.html', {'issue':issue,'answer':answer})


def Issues_list(request):
    if request.user.username == 'mica':
        issue_list = Issue.objects.all()
    else:
        P_no = Member.objects.filter(first_name=request.user.username).values_list('project_no')
        issue_list = Issue.objects.filter(project=P_no)

    return render(request, 'management/issues_list.html', {'issue_list':issue_list})

def Issues_Detail(request,issues_id):
    issues = Issue.objects.get(id=issues_id)
    project = Project.objects.get(project_no=issues.project_id)
    author = User.objects.get(id=issues.author_id)

    answer = Issue_Detail.objects.filter(issue_id=issues_id)

    form = IssueDetailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            issuedetail = form.save(commit=False)
            issuedetail.issue_id = issues_id
            issuedetail.replyer_id = request.user.id
            issuedetail.save()
            form = IssueDetailForm()
        else:
            form = IssueDetailForm()
    else:
        form = IssueDetailForm()

    return render(request, 'management/issues_detail.html',{'issues':issues, 'answer':answer, 'project':project, 'author':author, 'form':form})

def Profiles(request):
    if request.user.username == 'mica':
        Profiles = Member.objects.all()[:10]
    else:
        P_no = Member.objects.filter(first_name=request.user.username).values_list('project_no')
        Profiles = Member.objects.filter(project_no=P_no)
    #Profiles = Member.objects.all()[:10]
    #form = MembersForm(request.POST)
    #if form.is_valid():
    #    members = form.save(commit=False)
            #topic.num_responses = 1
    #    members.save()
            #return HttpResponseRedirect(reverse('management:'))

    return render(request, 'management/profiles.html',{'Profiles': Profiles})

def AddMember(request):
    form = MembersForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            messages.add_message(request, messages.SUCCESS, 'You have been submitted successfully!')
            form = MembersForm()
        else:
            messages.add_message(request, messages.ERROR, 'Error! Please check your input again!')
            form = MembersForm()
    else:
        form = MembersForm()
    return render(request, 'management/addmembers.html', {'form':form})


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

#def register(request):
#    employeelist = Employee.objects.all()
#    if request.method == 'POST':
#        form = RegisterForm(request.POST,request.FILES)
#        if form.is_valid():
#            employee = form.save(commit=False)
#            employee.save()
#            return HttpResponseRedirect(reverse('myapp:index'))
#    else:
#        form = RegisterForm()
#    return render(request, 'myapp/register.html',{'form':form, 'employeelist':employeelist})


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
            messages.add_message(request, messages.ERROR, 'Username and password are not matched. Please input again!')
            return render(request, 'management/login.html')
    else:
        return render(request, 'management/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:login')))

def user_register(request):
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return  HttpResponseRedirect(reverse('myapp:login'))
    else:
        form = MemberRegisterForm()
    return  render(request, 'management/register.html', {'form':form})


#def mycourses(request):
 #   courses = Course.objects.filter(students__username=request.user.username)
  #  return render(request, 'myapp/mycourses.html', {'courses': courses})