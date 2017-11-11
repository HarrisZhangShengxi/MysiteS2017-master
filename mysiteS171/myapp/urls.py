from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^task_creation1/$',views.AddProject),
        # url(r'^$', views.IndexView, name='index'),
        # url(r'^index0/$', views.IndexView, name='index'),
        # url(r'^index/$', views.index, name='index'),
        url(r'^(?P<course_no>\d+)/$', views.IssuesDetail, name='issues'),
        # url(r'^topics/$', views.topics, name='topics'),
        # url(r'^addtopic/$', views.addtopic, name='addtopic'),
        url(r'^topics/(?P<topic_id>\d+)/$', views.topicdetail, name='topicdetail'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^mycourses/$', views.mycourses, name='mycourses'),

]

