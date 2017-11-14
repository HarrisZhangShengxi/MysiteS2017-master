from django.conf.urls import url
from . import views

urlpatterns = [
      #  url(r'^base/$', views.base),
        url(r'^index/$', views.IndexView,name='index'),
        url(r'^addindex/$', views.AddAnRe),
        url(r'^addprojects/$',views.AddProject),
        url(r'^projects_list/$',views.Project_list),
        url(r'^addissues/$', views.AddIssues),
        url(r'^issues_list/$', views.Issues_list),
        url(r'^profiles/$', views.Profiles),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^addmembers/$',views.AddMember),

        # url(r'^$', views.IndexView, name='index'),

        # url(r'^index/$', views.index, name='index'),
        url(r'^issues_detail/(?P<issues_id>\d+)/$', views.Issues_Detail,name='issues_detail'),
        #url(r'^issues_detail/(?P<issues_id>\d+)/$', views.Issues_Detail,name='issues_detail'),
        # url(r'^topics/$', views.topics, name='topics'),




]

