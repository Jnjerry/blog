from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

# class is a special keyword that indicates that we are defining an object
#models.Model means that Post should be saved in the database
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(null=True ,blank=True,
                            width_field="width_field",
                            height_field="height_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)

    content=models.TextField(max_length=1000,)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True,blank=True,null=True)
    update=models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

      return reverse('detail',args=[str(self.id)])

    class Meta:
        ordering=["-timestamp","-update"]


class Comment(models.Model):
    post=models.ForeignKey('Post',related_name="comments")
    author = models.CharField(max_length=200)
    text= models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
         return self.text
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
