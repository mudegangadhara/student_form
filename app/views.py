from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Disply_student(request):
    FO=StudentForm()
    d={'FO':FO}
    if request.method == 'POST':
        FCD=StudentForm(request.POST)
        if FCD.is_valid():
            FCD.save()
            return HttpResponse('data is successfully saved')
        return HttpResponse('invalid data')
    return render(request, 'Disply_student.html',d)