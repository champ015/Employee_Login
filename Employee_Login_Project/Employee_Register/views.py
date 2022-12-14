from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
def Employee_List(request):
     context = {'employee_list': Employee.objects.all()}
     return render(request,"Employee_Register/Employee_List.html",context)
def Employee_Form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,"Employee_Register/Employee_Form.html",{'form':form})
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
           form.save()
        return redirect("/employee/list")
def Employee_Delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

# Create your views here.