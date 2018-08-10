from django.contrib import admin

from .models import Student, Teacher, Discipline

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Discipline)
# Register your models here.
