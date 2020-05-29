from django.db import models
from django.urls import reverse
from django.conf import settings

##allows for markdown / links in post
##
import misaka
from groups.model import Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
##POST MODELS.PY

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={'username':self.user.username,
                                               'pk':self._get_pk_val})
        
    class Meta:
        ordering= ['-created_at']
        
        ##every message is uniquely linked to user
        ##
        unique_together = ['user', 'message']
    
    
    


