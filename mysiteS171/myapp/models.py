from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Manager)
    description = models.CharField(max_length=100000)
    def __str__(self):
        return self.title

class Manager(User):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    age = models.IntegerField(null=True, blank=True)
  #  photo = models.ImageField(null=True, blank=True, upload_to='photos')
    def __str__(self):
        return self.last_name

class Project(models.Model):
    project_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    leader = models.CharField(max_length=50)
    start_date = models.TimeField()
    end_date = models.TimeField()

    Communication = 0
    Planning = 1
    Modeling = 2
    Construction = 3
    Deployment = 4
    phase_choice = (
        (0, 'Communication'),
        (1, 'Planning'),
        (2, 'Modeling'),
        (3, 'Construction'),
        (4, 'Deploylment')
    )
    phase = models.IntegerField(default=0, choices=phase_choice)
    description = models.CharField(max_length=100000)
    # textbook = models.ForeignKey(Book, null=True, blank=True)
    # students = models.ManyToManyField(Student, blank=True)
    def __str__(self):
        return str(self.project_no)+' '+ self.name

    # def __iter__(self):
    #     return self.title

class Task(models.Model):
    project_affiliation = models.ForeignKey(Project, null=True, blank=True)
    name = models.CharField(max_length=50)
    start_date = models.TimeField()
    due_date = models.TimeField()
    actual_end_date = models.TimeField()
    REQUIRED = 0
    SIGNIFICANT = 1
    MODERATE = 2
    MINOR = 3
    LOW = 4
    Priority_choice = (
        (0, 'Required'),
        (1, 'Significant'),
        (2, 'Moderate'),
        (3, 'Minor'),
        (4, 'Low')
    )
    priority = models.IntegerField(default=0, choices=Priority_choice)
    description = models.CharField(max_length=100000)
    def __str__(self):
        return self.name

class Issue(models.Model):
    object = models.CharField(max_length=1000)
    announcer = models.ForeignKey(Manager, null=True, blank=True)
    description = models.CharField(max_length=100000)
    def __str__(self):
        return self.object

class Answer(models.Model):
    answer = models.CharField(max_length=100000)
    replyer = models.ForeignKey(Manager, null=True, blank=True)
    object_no = models.ForeignKey(Issue, null=True, blank=True)