from django.db import models
from django.urls import reverse

# Create your models here.
##Mimim school admin site
###

class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    
    
class Student(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    ## want to match up with school above
    ##
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    