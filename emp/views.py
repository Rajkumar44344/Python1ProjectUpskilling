from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import FeedbackForm

# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        print("Data is comming")

        #data fetch from the request
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_phone")
        emp_department=request.POST.get("emp_department")




        #create model object and set the data
        emp=Emp()
        emp.name=emp_name
        emp.emp_id=emp_id
        emp.phone=emp_phone
        emp.address=emp_address
        
        emp.department=emp_department
        if emp_working is None:
            emp.working=False
        else:
            emp.working=True    

        


        #save the objct 
        emp.save()


        #prepare masg

        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})


#fucntion for delete emp code


def delete_emp(request,emp_id):
    print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")




#code for update emp
def update_emp(request, emp_id):
    emp = get_object_or_404(Emp, pk=emp_id)

    if request.method == "POST":
        print("Updating employee details...")

        # Fetch data from the request
        emp.name = request.POST.get("emp_name", emp.name)
        emp.emp_id = request.POST.get("emp_id", emp.emp_id)
        emp.phone = request.POST.get("emp_phone", emp.phone)
        emp.address = request.POST.get("emp_address", emp.address)
        emp_working = request.POST.get("emp_phone")
        emp.department = request.POST.get("emp_department", emp.department)

        # Update working status
        emp.working = False if emp_working is None else True

        # Save the object
        emp.save()

        # Redirect to home after successful update
        return redirect("/emp/home/")

    return render(request, "emp/update_emp.html", {"emp": emp})



def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request,"emp/testimonials.html",{
        'testi':testi
    })

def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("data Saved")
        else:
            return render(request,"emp/feedback.html",{'form':form})
  

    else:
        form=FeedbackForm()
        return render(request,"emp/feedback.html",{'form':form})

