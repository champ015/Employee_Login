from calendar import c
from sre_constants import MAX_UNTIL
from unittest.util import _MAX_LENGTH
from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
class Employee(models.Model):
    Full_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=20)
    Emp_Code=models.CharField(max_length=30)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)
     
     
    

# Create your models here.
