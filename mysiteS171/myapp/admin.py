# Register your models here.
from django.contrib import admin
from myapp.models import Member, Announcement, Manager, Project, Task, Issue, Answer
# Register your models here.



admin.site.register(Member)
admin.site.register(Announcement)
admin.site.register(Manager)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Issue)
admin.site.register(Answer)


class CourseAdmin (admin.ModelAdmin):
    filter_horizontal = ('students',)


class BookAdmin(admin.ModelAdmin):
  list_display=['title','author','numpages','in_stock']

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['first_name','last_name','get_courses']
    # def register_courses(self,obj):
    #     register_courses = list(Student.objects.get(first_name=obj.firstname).course_set.all())
    #     return register_courses
# admin.site.register(Student,StudentAdmin)
