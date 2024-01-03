from django.db import models

# Create your models here.
class tempModel(models.Model):
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.firstname