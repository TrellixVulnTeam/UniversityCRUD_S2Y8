from django.db import models

class Student(models.Model):
    student_id_num = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subscription_date = models.DateTimeField('Subscription Date')
    year = models.IntegerField(default=1)
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
        return self.last_name
    

class Discipline(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    workload = models.IntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name, self.description

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date_of_enrollment = models.DateField('enrollment date')
    date_of_end = models.DateField('finish date')

        
