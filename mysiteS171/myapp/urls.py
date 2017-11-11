from django.conf.urls import url
from . import views

urlpatterns = [
        # url(r'^$', views.IndexView, name='index'),
        url(r'^index/$', views.IndexView, name='index'),
        # url(r'^index/$', views.index, name='index'),
        # url(r'^(?P<issues_no>\d+)/$', views.IssuesDetail, name='issues'),
        # url(r'^topics/$', views.topics, name='topics'),
        url(r'^issueslist/$', views.IssuesListView, name='issueslist'),
        url(r'^issues/(?P<issues_no>\d+)/$', views.IssuesDetail, name='issuesdetail'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^mycourses/$', views.mycourses, name='mycourses'),
        url(r'^task_creation/$',views.AddProject,)
]

