from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^base/$', views.base, name="base"),
        url(r'^index/$', views.IndexView, name="index"),
        url(r'^addprojects/$',views.AddProject, name="addprojects"),
        url(r'^projects_list/$',views.Project_list, name="projectslist"),
        url(r'^issues/id=(?P<id>\d+)$', views.Issues_Detail, name="issues"),
        url(r'^issues_list/$', views.Issues_list, name="issueslist"),
        # url(r'^solutions/$', views.Solution),
        url(r'^profiles/$', views.Profiles, name="profiles"),
        url(r'^index/addindex/$', views.AddAnRe, name="addindex"),

        # url(r'^$', views.IndexView, name='index'),

        # url(r'^index/$', views.index, name='index'),
        # url(r'^(?P<issues_no>\d+)/$', views.IssuesDetail, name='issues'),
        # url(r'^topics/$', views.topics, name='topics'),


        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),

        url(r'^logout/$', views.user_logout, name='logout'),


]

