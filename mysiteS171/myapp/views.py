from django.shortcuts import render,render_to_response
from models import Announcement, User, Task, Project, Answer, Issue, Requirement
from forms import SolutionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

# class IndexView(ListView):
#     model= Course
#     context_object_name='courselist'
#     template_name='myapp/index.html'

#class_based view

def AnnouncementView(request):
     # def get(self, request):
        acmt_list = Announcement.objects.all()
        # register_form = RegisterForm()
        # Deal with cookies
        # if request.session.get('last_visit'):
        #     last_visit_time = request.session.get('last_visit')
        #     visits = request.session.get('visits', 0)
        #
        #     # Use seconds instead of days for testing
        #     if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 0:
        #         request.session['visits'] = visits + 1
        #         request.session['last_visit'] = str(datetime.now())
        # else:
        #     # this code was never reached, so the session was not being set
        #     request.session['last_visit'] = str(datetime.now())
        #     request.session['visits'] = 1
        #
        # if request.session.get('visits'):
        #     count = request.session.get('visits')
        # else:
        #     count = 0
        #
        # context = {
        #         'course_list':course_list,
        #         'count': count
        #
        #     }
        return render(request,'management/index.html',{'acmtlist':acmt_list})

def RequirementView(request):
    remt_list = Requirement.objects.all()
    return render(request,'management/index.html',{'remtlist':remt_list})

def IssuesListView(request):
    issue_list = Issue.objects.all()
    return render(request, 'management/issues_list.html', {'issuelist':issue_list})

def IssuesDetail(request, issues_no):
    issue = Issue.objects.filter(id=issues_no)
    return render(request, 'management/issues.html', {'issue':issue})

def Solution(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.num_responses = 1
            solution.save()
            return HttpResponseRedirect(reverse('management:issues'))
    else:
        form = SolutionForm()
    return render(request, 'management/issues.html')

def AddPrject(request):
    topiclist = Project.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses = 1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form = TopicForm()
    return render(request, 'myapp/addtopic.html',{'form':form, 'topiclist':topiclist})

def topicdetail(request, topic_id):
    topic = Topic.objects.filter(id=topic_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid() and request.POST.get('interested') == '1':
            interested = form.cleaned_data['interested']
            age = form.cleaned_data['age']
            for t in topic:
                n = t.num_responses + 1
                topic.update(num_responses=n)
                a = (t.avg_age * t.num_responses + int(request.POST.get('age'))) / n
                topic.update(avg_age=a)
            return HttpResponseRedirect(reverse('myapp:topics'))
        else:
            return HttpResponseRedirect(reverse('myapp:topics'))
    elif request.method == 'GET':
        form = InterestForm()
    return render(request, 'myapp/topicdetail.html', {'form': form, 'topic': topic})

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

def mycourses(request):
    courses = Course.objects.filter(students__username=request.user.username)
    return render(request, 'myapp/mycourses.html', {'courses': courses})