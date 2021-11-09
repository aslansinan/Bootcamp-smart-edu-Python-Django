from django.db import models
class Course(models.Model):
    name=models.CharField(max_length=200,unique=True)
    description=models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/")
    date = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


