from django.db import models

# Create your models here.
class Dept(models.Model):
    deptid=models.IntegerField(primary_key=100)
    deptname=models.CharField(max_length=100)
    deptloc=models.CharField(max_length=100)

class Emp(models.Model):
    empid=models.IntegerField(primary_key=True  )
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=3)
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    hiredate=models.DateField()
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    deptid=models.ForeignKey(Dept,on_delete=models.CASCADE)