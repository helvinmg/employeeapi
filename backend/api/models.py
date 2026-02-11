from django.db import models
# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    salary=models.FloatField()

    def __str__(self):
        return self.name+" - "+self.designation
