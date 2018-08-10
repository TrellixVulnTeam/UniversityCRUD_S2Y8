from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import Student, Discipline, Teacher


# ----------- STUDENTS View Methods ----------- #

def students_index(request):
    # order_by('-subscription_date')[:5]
    latest_subscribers_list = Student.objects.order_by('-first_name')[:5]
    return render (request, 'students/index.html', {'latest_subscribers_list': latest_subscribers_list})

def students_detail(request, student_id_num):
    try:
        student = Student.objects.get(pk=student_id_num)
    except Student.DoesNotExist:
        raise Http404("Student does't exist")
    return render(request, 'students/detail.html', {'student': student})
    

def students_delete(request, student_id_num):
    try:
        Student.objects.get(pk=student_id_num).delete()      
    except Student.DoesNotExist:
        raise Http404("Student not found")
    return render(request, 'students/index.html', {})


# ----------- DISCIPLINES View Methods ----------- #

def disciplines_index(request):
    list_disciplines = Discipline.objects.all()
    return render(request, 'disciplines/index.html',{'list_disciplines': list_disciplines})

def disciplines_create(request):
    if request.method == 'GET':
        list_teachers = Teacher.objects.all()
        return render(request, 'disciplines/create.html', {'list_teachers': list_teachers})

    if request.method == 'POST':
        try:            
            discipline_teacher = request.POST['teacher']
            if not discipline_teacher:                
                discipline_name = request.POST['name']
                #discipline_workload = request.POST['workload']
                #discipline_description = request.POST['description']
                #discipline = Discipline.create(
                #    teacher=discipline_teacher,name=discipline_name,workload=discipline_workload,description=discipline_description)
                #if discipline.save():
                return HttpResponse(discipline_teacher)
            else:
                raise Http404("Teacher not found!")        
        except:
             raise Http404("Could not add discipline")
    return render(request, 'disciplines/index.html', {})
        

def disciplines_detail(request, id):
    try:
        discipline = Discipline.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Discipline does't exist")
    return render(request, 'disciplines/detail.html', {'discipline': discipline})


# ----------- TEACHERS View Methods ----------- #

def teachers_index(request):
    list_of_teachers = Teacher.objects.all()
    return render (request, 'teachers/index.html', {'list_of_teachers': list_of_teachers})


def teachers_detail(request, teacher_id_number):
    try:
        teacher = Teacher.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Teacher does't exist")
    return render(request, 'students/detail.html', {'teacher': teacher})