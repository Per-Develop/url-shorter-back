from django.db import models

# Create your models here.

class Addr(models.Model):
    longaddr = models.CharField(max_length=1000)
    shortaddr = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.longaddr