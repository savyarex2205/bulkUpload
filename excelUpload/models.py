from django.db import models

# Create your models here.
class userModel(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
