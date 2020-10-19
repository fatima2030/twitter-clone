from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



# Create your models here.

class Post(models.Model): 
    content = models.TextField(max_length=500)
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    def __str__(self):
        return self.content[:5] 
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    def numbcount_post(user):
        return Post.objects.filter(author=user).count()
   


class Comment(models.Model):
    cotent = models.TextField(max_length=140)
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post,on_delete=models.CASCADE) 
    

class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now= True)



    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")

