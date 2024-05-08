from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from app.models import *

def insert_dept(request):
    dt=int(input('Enter dept no : '))
    dn=input('Enter dept name : ')
    dl=input('Enter Location : ')
    DO=Dept.objects.get_or_create(DEPTNO=dt,DNAME=dn,LOC=dl)[0]
    DO.save()

    return HttpResponse('create all the dept information successfully')

def display_dept(request):
    QDLO=Dept.objects.all()
    d={'QDLO':QDLO}
    return render(request,'display_dept.html',d)
        

def insert_emp(request):
    do=int(input('Enter dept : '))
    DO=Dept.objects.filter(DEPTNO=do)

    if DO:
        eno=int(input('Enter emp no : '))
        en=input('Enter emp name : ')
        j=input('Enter emp job : ')

        MTO=input('Enter mgr : ')

        if MTO:
            MEO=Emp.objects.get(Emp_no=int(MTO))
        else:
            MEO=None

        h=input('Enter hiredate : ')
        s=int(input('Enter emp salary : '))
        COMM=input('Enter commition : ')


        if COMM:
            COMM=int(COMM)
        else:
            COMM=None
        
        EO=Emp.objects.get_or_create(Emp_no=eno,ENAME=en,JOB=j,MGR=MEO,HIREDATE=h,SAL=s,COMM=COMM,DEPTNO=DO[0])[0]
        EO.save()
        
        return HttpResponse('Create emp table successfully')

    else:
        return HttpResponse('Given deptno is not there in dept table')
    
    
def display_emp(request):
    QELO=Emp.objects.all()
    QELO=Emp.objects.filter(ENAME__startswith='j')
    QELO=Emp.objects.filter(ENAME__startswith='a',ENAME__endswith='n')
    QELO=Emp.objects.filter(Q(ENAME__startswith='j') | Q(ENAME__contains='e'))
    QELO=Emp.objects.filter(HIREDATE__gt='1982-01-01')
    QELO=Emp.objects.filter(HIREDATE__gt='1982-01-01',HIREDATE__lt='1987-12-31')
    QELO=Emp.objects.filter(HIREDATE__gte='1981-04-04',HIREDATE__lte='1987-05-23')
    QELO=Emp.objects.filter(Q(ENAME__startswith='j') & Q(ENAME__contains='e') | Q(HIREDATE__gt='1982-01-01'))
    QELO=Emp.objects.filter(SAL__range=(2000,20000))
    QELO=Emp.objects.filter(Q(SAL__range=(0,1200)) | Q(SAL__range=(1300,3000)))
    QELO=Emp.objects.filter(DEPTNO=30)
    QELO=Emp.objects.filter(Q(JOB='salesman') & Q(ENAME__startswith='a') | Q(ENAME__contains='e'))
    QELO=Emp.objects.filter(Q(JOB='salesman') & Q(ENAME__startswith='a') | Q(ENAME__contains='e') | Q(ENAME__startswith='j') & Q(ENAME__contains='e') | Q(HIREDATE__gt='1982-01-01'))

    
    
    d={'QELO':QELO}
    return render(request,'display_emp.html',d)

def insert_sal(request):
    gr=int(input('Enter grade : '))
    lo=int(input('Enter losal : '))
    ho=int(input('Enter hosal : '))

    SO=Salary.objects.get_or_create(GRADE=gr,LOSAL=lo,HISAL=ho)[0]
    SO.save()

    return HttpResponse('create successfully')

def display_sal(request):
    QSLO=Salary.objects.all()
    d={'QSLO':QSLO}
    return render(request,'display_sal.html',d)