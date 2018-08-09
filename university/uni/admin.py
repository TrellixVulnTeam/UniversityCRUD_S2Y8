from django.contrib import admin

from .models import Student, Teacher, Discipline, Enrollment

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Enrollment)
# Register your models here.
