from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):

    user = models.ForeignKey(User,on_delete= models.CASCADE,null=True,blank=True)


    title = models.CharField(max_length=100)
    description =models.TextField()
    image1 = models.ImageField(upload_to='featured_image/') 
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class  Meta:
        ordering = ['complete'] 



