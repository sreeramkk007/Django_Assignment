from django.db import models

# Create your models here.
class register(models.Model):
    
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=200,null=True)
    gender_option=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    gender = models.CharField(max_length=6, choices=gender_option)

    def __str__(self):
        return self.firstname

   