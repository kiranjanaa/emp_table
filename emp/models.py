from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=100)
    dept_name=models.CharField(max_length=100)
    dept_loc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.dept_no)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=3)
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    hiredate=models.DateField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.empno)

    