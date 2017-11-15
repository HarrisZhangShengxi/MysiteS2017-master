from datetime import date

from django.shortcuts import render,render_to_response

from .models import Announcement, Requirement,  Project, Issue, Member, Issue_Detail
from .forms import ProjectForm, AnnouncementForm,RequirementForm,IssuesForm,MembersForm,IssueDetailForm
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
    if Aform.is_valid():
        announcement = Aform.save(commit=False)
        announcement.date = date.today()
        announcement.save()
    else:
        Aform = AnnouncementForm()

    Rform = RequirementForm(request.POST)
    if Rform.is_valid():
        requirement = Rform.save(commit=False)
        requirement.date = date.today()
        requirement.save()
    else:
        Rform = RequirementForm()

    return render(request, 'management/addindex.html', {'Aform': Aform, 'Rform': Rform})

def AddProject(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
    else:
        form = ProjectForm()

    return render(request, 'management/addprojects.html', {'form': form})

def Project_list(request):
    member = Member.objects.filter(first_name=request.user.username)
    Project_list = Project.objects.filter(members=member)
    return render(request, 'management/projects_list.html', {'Project_list': Project_list})

def AddIssues(request):
    form = IssuesForm(request.POST)
    if form.is_valid():
        issue = form.save(commit=False)
        issue.date = date.today()
        issue.save()
        # return HttpResponseRedirect(reverse('management:'))
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
    if form.is_valid():
        issuedetail = form.save(commit=False)
        issuedetail.save()
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
    if form.is_valid():
        member = form.save(commit=False)
        member.save()
        user = User.objects.create_user(username=member.first_name,password="haohaoxuexi")
        user.save()
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
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'management/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))

#def mycourses(request):
 #   courses = Course.objects.filter(students__username=request.user.username)
  #  return render(request, 'myapp/mycourses.html', {'courses': courses})