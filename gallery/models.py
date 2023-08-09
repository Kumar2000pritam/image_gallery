from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Pictures(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    pic=models.ImageField(upload_to ='')
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.pic.url}" width ="300"/>')
    
class Feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback
