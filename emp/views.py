from django.shortcuts import render
from django.http import HttpResponse
from emp.models import *
# Create your views here.
def insert_Dept(request):
    dept_no=int(input("enter dept number : "))
    dept_name=input("enter dept ename : ")
    dept_loc=input("enter dept loc : ")
    DTO=Dept.objects.get_or_create(dept_no=dept_no,dept_name=dept_name,dept_loc=dept_loc)
    if DTO[1]:
        return HttpResponse("new dept table is created")
    else:
        return HttpResponse("Given dept table is already present")



def insert_Emp(request):
    empno=int(input("enter the empnumber : "))
    empname=input("enter the emp name : ")
    job=input("enter the job name : ")
    sal=int(input("enter the sal : ")) 
    comm=input("enter the comm : ")
    if comm:
        comm=int(comm)
    else:
        comm=None
    hiredate=input("enter the employee date : ")
    deptno=int(input("enter dept number : "))
    mgr=input("enter mgr number : ")
    if mgr:
        mgr=int(mgr)
        mgr=Emp.objects.filter(empno=mgr)
    else:
        mgr=None
   
    DLOB=Dept.objects.filter(dept_no=deptno)
    print(DLOB)
    if DLOB:
        ETO=Emp.objects.get_or_create(empno=empno,empname=empname,job=job,sal=sal,comm=comm,hiredate=hiredate,deptno=DLOB[0],mgr=mgr)
        if ETO[1]:
            return HttpResponse("EMP object is created")
        else:
            return HttpResponse("Employee object  is already present")
    else:
        return HttpResponse("dept objects is not present")

def dispalay_Dept(request):
    LTO=Dept.objects.all()
    D={'LTO':LTO}
    return render(request,'display_Dept.html',D)

def display_Emp(request):
    EOP=Emp.objects.all()
    D={'EOP':EOP}
    return render(request,'display_Emp.html',D)


