from django.db import models

# Create your models here.






class UserProfile(models.Model):
    # id = models.BigIntegerField()
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    bio = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)
    
    


def __str__(self):
        return self.task