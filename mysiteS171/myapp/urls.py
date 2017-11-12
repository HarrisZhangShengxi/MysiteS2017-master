from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^base/$', views.base),
        url(r'^index/$', views.IndexView),
        url(r'^addprojects/$',views.AddProject),
        url(r'^projects_list/$',views.Project_list),
        url(r'^issues/$', views.Issues_Detail),
        url(r'^issues_list/$', views.Issues_list),
        url(r'^solutions/$', views.Solution),
        url(r'^profiles/$', views.Profiles),

        # url(r'^$', views.IndexView, name='index'),

        # url(r'^index/$', views.index, name='index'),
        # url(r'^(?P<issues_no>\d+)/$', views.IssuesDetail, name='issues'),
        # url(r'^topics/$', views.topics, name='topics'),


        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),

        url(r'^logout/$', views.user_logout, name='logout'),


]

