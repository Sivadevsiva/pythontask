from django.db import models

# Create your models here.



class school_tab(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.TextField()
    phoneno=models.TextField()
    email=models.EmailField()
    address = models.TextField(max_length=250)
    debitnotebook = models.TextField(default=True)
    pen = models.TextField(default=True)
    exampaper = models.TextField(default=True)



    def __str__(self):
        return self.name



