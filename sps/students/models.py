from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    student_id = models.CharField(max_length=100)
    phy=models.IntegerField(default=90)
    chem=models.IntegerField(default=90)
    bio=models.IntegerField(default=90)
    maths=models.IntegerField(default=90)
    pcb=models.IntegerField(default=90)
    pcm=models.IntegerField(default=90)
    

    def __str__(self):
        return self.firstname 
    


    

