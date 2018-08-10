from django.db import models

class Student(models.Model):
    student_id_num = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subscription_date = models.DateTimeField('Subscription Date')
    YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    )
    year_in_school = models.CharField(
        max_length = 2,
        choices = YEAR_IN_SCHOOL_CHOICES,
        default = 'FR',
    )

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    teacher_id_number = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subscription_date = models.DateField('subscription date')
    AREA_OF_DOMAIN_CHOICES = (
        ('CE', 'College of Engineering'),
        ('CAS', 'College of Arts and Sciences'),
        ('IA','International Affairs' ),
        ('MCS', 'Mathematics and Computer Science'),
        ('MHS', 'Medicine and Health Sciences'),
    )
    area_of_domain = models.CharField(
        max_length=3,
        choices = AREA_OF_DOMAIN_CHOICES,
        default='CE',
    )

    def __str__(self):
        template = '{0.last_name} {0.first_name} {0.subscription_date}'
        return template.format(self)
    

class Discipline(models.Model):
    discipline_id_num = models.CharField(max_length=20, primary_key=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    workload = models.IntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        template = '{0.name} {0.description} {0.workload}'
        return template.format(self)


        
