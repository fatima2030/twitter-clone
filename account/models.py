from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from PIL import Image

from cloudinary.models import CloudinaryField


# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image =CloudinaryField('image')


    def __str():
        return f'{user.username} Profile'


    @property
    def follwers(self):  
        return Follw.objects.filter(follow_user=self.user).count() 
    
    @property
    def following(self):
        return Follw.objects.filter(user=self.user).count()
    def numbcount_post(self):
        return Post.objects.filter(author=self.user).count()


    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        super().save()

        imag=Image.open(self.image.path)
        if imag.height>300 or imag.width> 300:
            output_size(300,300)
            imag.thumbnail(output_size)
            imag.save(self.image.path)

 

class Follw(models.Model):
    user = models.ForeignKey(User,related_name='user' , on_delete = models.CASCADE)
    follow_user= models.ForeignKey(User,related_name='follow_user',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

