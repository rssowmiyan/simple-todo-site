from django.db import models
from django.contrib.auth.models import  User

class Getitdone(models.Model): 
    title=models.CharField(max_length=100)
    memo=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(blank=True,null=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title