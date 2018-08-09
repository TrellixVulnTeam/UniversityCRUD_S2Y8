from django.http import Http404
from django.shortcuts import render
from .models import Student

def index(request):
    # order_by('-subscription_date')[:5]
    latest_subscribers_list = Student.objects.order_by('-first_name')[:5]
    context = {
        'latest_subscribers_list': latest_subscribers_list,
    }
    return render (request, 'students/index.html', context)

def detail(request, student_id_num):
    try:
        student = Student.objects.get(pk=student_id_num)
    except Student.DoesNotExist:
        raise Http404("Student does't exist")
    return render(request, 'students/detail.html', {'student': student})
    

# def summary(request, student_id_num):
#     response = "Summary of student: %s." + % student_id_num
#     return HttpResponse(response % student_id_num)


