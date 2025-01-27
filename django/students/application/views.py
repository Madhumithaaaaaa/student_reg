from django.shortcuts import render
from.models import Datas

# Create your views here.

def home(request):
    return render(request,'index.html')


def register_form_submission(request):
    if request.method=='POST':
        var1=Datas(Student_Name=request.POST.get('Student_Name'),
                   First_Name=request.POST.get('First_Name'),
                   Middle_Name=request.POST.get('Middle_Name'),
                   Last_Name=request.POST.get('Last_Name'),
                   Date_of_Birth=request.POST.get('Date_of_Birth'),
                   Mobile_Number=request.POST.get('Mobile_Number'),
                   Email_Address=request.POST.get('Email_Address'),
                   Address=request.POST.get('Address'))  
        var1.save()
        return render(request,'index.html')             

