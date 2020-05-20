from django.db import models

# Create your models here.
class Topic(models.Model):
    ## Max Length is constraint
    ## Otherwise users can put whatever length they want
    ##
    top_name = models.CharField(max_length = 264, unique= True)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    ## columns for database
    ##
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        ## return name of webpage
        ##
        return self.name
    
class AccessRecord(models.Model):
    
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)