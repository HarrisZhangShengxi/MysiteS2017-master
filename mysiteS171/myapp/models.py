from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, unique=True)
    description = models.CharField(max_length=100000)
    date = models.DateTimeField()
    def __str__(self):
        return self.title

class Requirement(models.Model):
    title = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    date = models.DateTimeField()
    def __str__(self):
        return self.title

class User(User):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(max_length=15)
    def __str__(self):
        return self.first_name, self.last_name

class Project(models.Model):
    project_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    leader = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

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

class Task(models.Model):
    project_affiliation = models.ForeignKey(Project, null=True, blank=True)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    due_date = models.DateField()
    actual_end_date = models.DateField()
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
    announcer = models.ForeignKey(User, unique=True)
    description = models.CharField(max_length=100000)
    time =  models.DateTimeField()
    def __str__(self):
        return self.object

class Answer(models.Model):
    answer = models.CharField(max_length=100000)
    replyer = models.ForeignKey(User, unique=True)
    issue_no = models.ForeignKey(Issue, unique=True)