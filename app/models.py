from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=20,unique=True)
    LOC=models.CharField(max_length=20)

    def __str__(self):
        return str(self.DEPTNO)


class Emp(models.Model): 
    Emp_no=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=50)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ENAME

class Salary(models.Model):
    GRADE=models.IntegerField()
    LOSAL=models.DecimalField(max_digits=10,decimal_places=2)
    HISAL=models.IntegerField()

    def __str__(self):
        return str(self.HISAL)